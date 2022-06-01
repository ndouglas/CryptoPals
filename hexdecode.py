import sys
arg1 = bytes.fromhex(sys.argv[1])
print(arg1.decode('ascii'))
