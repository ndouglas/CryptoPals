import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]


def get_bit_difference(char1, char2):
    return bin(ord(char1) ^ ord(char2)).count("1")


def get_hamming_difference(str1, str2):
    result = 0
    for idx in range(len(str1)):
        result += get_bit_difference(str1[idx], str2[idx])
    return result


print(get_hamming_difference(arg1, arg2))
