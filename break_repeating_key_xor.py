import base64
import sys

arg1 = sys.argv[1]


def get_bit_difference(char1, char2):
    return bin(ord(char1) ^ ord(char2)).count("1")


def get_hamming_difference(str1, str2):
    result = 0
    for idx in range(len(str1)):
        char1 = str1[idx]
        char2 = str2[idx] if idx < len(str2) else ' '
        result += get_bit_difference(char1, char2)
    return result


def get_hamming_difference_for_keysize(keysize, str):
    chunks = split_text_by_keysize(str, keysize)
    diffs = []
    for i in range(1, len(chunks)):
        diff = get_hamming_difference(chunks[i - 1], chunks[i])
        diffs.append(diff)
    average_diff = sum(diffs) / len(diffs)
    normalized_diff = average_diff / keysize
    return normalized_diff


def get_most_probable_keysizes(str):
    scores = {}
    for keysize in range(2, min(40, len(str)//2)):
        score = get_hamming_difference_for_keysize(keysize, str)
        scores[keysize] = score
    sorted_scores = list(sorted(scores.items(), key=lambda x: x[1]))
    return [i[0] for i in sorted_scores[0:3]]


def split_text_by_keysize(str, keysize):
    chunks = len(str)
    return [str[i:i+keysize] for i in range(0, chunks, keysize)]


def transpose_chunks(text_chunks):
    result = []
    for i in range(len(text_chunks[0])):
        this_chunk = ''
        for chunk in text_chunks:
            this_chunk += chunk[i] if i < len(chunk) else ''
        result.append(this_chunk)
    return result


def score_string(str):
    result = 0
    for char in str.lower():
        if char == 'e':
            result += 12
        elif char == 't':
            result += 9
        elif char in ['a', 'i', 'o', 'n', 's']:
            result += 8
        elif char in ['h', 'r']:
            result += 6
        elif char in ['d', 'l', 'u']:
            result += 4
        elif char in ['c', 'f']:
            result += 3
        elif char in ['w', 'y', 'g', 'p', 'b']:
            result += 2
        elif char in ['v', 'k', 'q', 'j', 'x', 'z']:
            result += 1
        elif char in ['\'', ',', '.', ' ', ':', '"', '-']:
            result += 0
        else:
            result -= 10
    return result


def get_best_keybyte(str):
    highest_score = 0
    strings = []
    scores = []
    result = 0
    for char in range(128):
        xored_bytes = bytes([ord(a) ^ char for a in str])
        string = xored_bytes.decode('ascii')
        score = score_string(string)
        strings.append(string)
        scores.append(score)
        if score > highest_score:
            highest_score = score
            result = char
    return result


def get_key(str, keysize):
    text_chunks = split_text_by_keysize(str, keysize)
    transposed_chunks = transpose_chunks(text_chunks)
    keystring = ''
    for chunk in transposed_chunks:
        this_keybyte = get_best_keybyte(chunk)
        keystring += chr(this_keybyte)
    return keystring


def get_keys(str):
    keysizes = get_most_probable_keysizes(str)
    keys = []
    for keysize in keysizes:
        keys.append(get_key(str, keysize))
    return keys


def decode_string(str, key):
    string = ''
    for idx, char in enumerate(str):
        key_char = key[idx % len(key)]
        string_char = chr(ord(key_char) ^ ord(char))
        string += string_char
    return string


def get_best_key(keys):
    best_key = None
    best_key_score = 0
    for key in keys:
        key_score = score_string(key)
        if key_score > best_key_score:
            best_key = key
            best_key_score = key_score
    return best_key


def break_string(str):
    keys = get_keys(str)
    key = get_best_key(keys)
    result = decode_string(str, key)
    return result


def break_file(filename):
    file_content = ''
    with open(filename) as line_file:
        for line in line_file:
            file_content += line.strip()
    str = base64.b64decode(file_content).decode('ascii')
    return break_string(str)


print(break_file(arg1))
