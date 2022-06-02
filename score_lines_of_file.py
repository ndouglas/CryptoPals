import sys


def score_string(string):
    result = 0
    for char in string.lower():
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
        else:
            result -= 10
    return result


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


with open('s1c4.txt') as line_file:
    highest_score = 0
    best_string = ''
    for line in line_file:
        (score, string) = get_best_string(line)
        if score > highest_score:
            highest_score = score
            best_string = string
    print(best_string)
