import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2] if sys.argv[2] else 20
while len(arg1) < int(arg2):
    arg1 += "\x04"
print(arg1)
print(len(arg1))
