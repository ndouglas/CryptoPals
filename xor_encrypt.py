import base64
import sys

key = sys.argv[1]
string = sys.argv[2]
bytes = []

for i, char in enumerate(string):
    key_char = key[i % len(key)]
    bytes.append("{:02x}".format(ord(key_char) ^ ord(char)))

print(''.join(bytes))
