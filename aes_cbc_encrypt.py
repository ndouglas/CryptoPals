import base64
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import sys
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES


encoding = 'ascii'


def xor(bytes1, bytes2):
    return ''.join([chr(a ^ b).lstrip("0x") for a, b in zip(bytes1, bytes2)])


def encrypt(key, raw):
    raw = pad(raw)
    cipher = AES.new(key.encode(encoding), AES.MODE_ECB)
    return b64encode(cipher.encrypt(raw.encode(encoding)))


def decrypt(key, enc):
    cipher = AES.new(key.encode(encoding), AES.MODE_ECB)
    output = cipher.decrypt(enc)
    return output


def get_file(filename):
    file_content = ''
    with open(filename) as line_file:
        for line in line_file:
            file_content += line.strip()
    return bytes(file_content, encoding)


def encrypt_cbc(key, raw, iv):
    chunks = split_text(file_raw, 16)
    result = ''
    last = iv
    for chunk in chunks:
        curr = xor(chunk, last)
        result += encrypt(key, curr)
        last = curr


def decrypt_cbc(key, enc, iv):
    chunks = split_text(enc, 16)
    result = ''
    last = iv
    for chunk in chunks:
        curr = chunk
        decrypted = decrypt(key, chunk)
        xored = xor(bytes(decrypted), last)
        result += xored
        last = curr
    return result


def split_text(str, size):
    str = b64decode(str)
    chunks = len(str)
    return [str[i:i+size] for i in range(0, chunks, size)]


iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
key = sys.argv[1]
filename = sys.argv[2]

file_raw = get_file(filename)
print(decrypt_cbc(key, file_raw, iv))
