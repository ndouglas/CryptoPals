from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import sys
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
encoding = 'ascii'


def encrypt(key, raw):
    raw = pad(raw)
    cipher = AES.new(key.encode(encoding), AES.MODE_ECB)
    return b64encode(cipher.encrypt(raw.encode(encoding)))


def decrypt(key, enc):
    enc = b64decode(enc)
    cipher = AES.new(key.encode(encoding), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16).decode(encoding)


def get_file(filename):
    file_content = ''
    with open(filename) as line_file:
        for line in line_file:
            file_content += line.strip()
    return bytes(file_content, encoding)


arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(decrypt(arg1, get_file(arg2)))
