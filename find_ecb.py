import sys
from collections import Counter


def get_best_string(str):
    highest_score = 0
    strings = []
    scores = []
    best_string = ''
    for char in range(128):
        try:
            xored_bytes = bytes([a ^ char for a in bytes.fromhex(str)])
            string = xored_bytes.decode('ascii')
            score = score_string(string)
            strings.append(string)
            scores.append(score)
            if score > highest_score:
                highest_score = score
                best_string = string
        except:
            pass
    return (highest_score, best_string)


def split_text(str, size):
    chunks = len(str)
    return [str[i:i+size] for i in range(0, chunks, size)]


with open('s1c8.txt') as line_file:
    for line in line_file:
        chunks = split_text(line, 16)
        expected_count = len(chunks)
        unique_chunks = Counter(chunks).keys()
        actual_count = len(unique_chunks)
        if actual_count < expected_count:
            print("line: ", line)
            print("chunks: ", chunks)
            print("has unique chunks: ", actual_count)
