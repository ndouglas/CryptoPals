import sys
arg1 = bytes.fromhex(sys.argv[1])


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
        elif char in ['\'', ',', '.', ' ']:
            result += 0
        else:
            result -= 10
    return result


highest_score = 0
strings = []
scores = []
best_string = ''
for char in range(128):
    xored_bytes = bytes([a ^ char for a in arg1])
    string = xored_bytes.decode('ascii')
    score = score_string(string)
    strings.append(string)
    scores.append(score)
    if score > highest_score:
        highest_score = score
        best_string = string
print(best_string)
