#!/usr/bin/env python3
from Crypto.Cipher import AES
import base64
import json
import argparse
import sys

SALT = b'tu89geji340t89u2'
KEY = b'\xa7\xca\x9f3f\xd8\x92\xc2\xf0\xbe\xf4\x174\x1c\xa9q\xb6\x9a\xe9\xf7\xba\xcc\xcf\xfc\xf4<b\xd1\xd7\xd0!\xf9'
CIPHER = AES.new(KEY, AES.MODE_CBC, SALT)


def decrypt(save: str) -> dict:
    save = base64.b64decode(save)
    save = CIPHER.decrypt(save)
    padding_symbol = save[-1]
    if padding_symbol < 16:
        save = save[:-padding_symbol]
    return json.loads(save)


def encrypt(save: dict) -> str:
    save = json.dumps(save, separators=(',', ':'))
    save = save.encode()
    tail = len(save) % 16
    if tail > 0:
        padding_symbol = 16 - tail
        save += bytes((padding_symbol,)) * padding_symbol
    save = CIPHER.encrypt(save)
    return base64.b64encode(save).decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='script for encrypting/decrypting Fallout Shelter *.sav files')
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="decrypt save data", default=False)
    args = parser.parse_args()
    data = sys.stdin.read()
    if args.decrypt is True:
        data = decrypt(data)
        data = json.dumps(data, sort_keys=True, indent=4)
    else:
        data = json.loads(data)
        data = encrypt(data)
    sys.stdout.write(data)
