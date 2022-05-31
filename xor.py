import base64
import sys

arg1 = bytes.fromhex(sys.argv[1])
arg2 = bytes.fromhex(sys.argv[2])
print(''.join([hex(a ^ b).lstrip("0x") for a, b in zip(arg1, arg2)]))
