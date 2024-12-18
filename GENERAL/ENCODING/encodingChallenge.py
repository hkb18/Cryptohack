from pwn import *
import json
import base64
import binascii
import codecs
import sys

def decode(t, data):
    if t == 'base64':
        return base64.b64decode(data).decode('utf-8')
    elif t == 'hex':
        return binascii.unhexlify(data).decode('utf-8')
    elif t == 'bigint':
        return binascii.unhexlify(data.replace('0x', '')).decode('utf-8')
    elif t == 'rot13':
        return codecs.encode(data, 'rot_13')
    elif t == 'utf-8':
        s = ""
        for c in data:
            s += chr(c)
        return s


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:

    received = json_recv()

    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    to_send = {
        "decoded": decode(received["type"], received["encoded"])
    }
    json_send(to_send)

    # This script interacts with a remote server to decode various encoded messages based on their specified encoding type (e.g., base64, hex, bigint, rot13, utf-8). The program automates decoding by identifying the encoding type and applying the appropriate method, aiming to extract a hidden flag. The challenge tests understanding of different encoding schemes and the ability to handle automated decoding in a structured way.