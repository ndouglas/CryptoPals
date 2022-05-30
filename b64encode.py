import base64
import sys

print(base64.b64encode(bytes.fromhex(sys.argv[1])))
