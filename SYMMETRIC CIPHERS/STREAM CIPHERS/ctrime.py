import requests, sys

solution = "crypto{"
chars = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789_abcdefghijklmnopqrstuvwxyz}'
invalid_char = ';'

while True:
    p = (solution + invalid_char) * 2
    r = requests.get("https://aes.cryptohack.org/ctrime/encrypt/" + p.encode('ascii').hex()).json()
    sample = len(r['ciphertext'])
    for c in chars:
        r = requests.get("https://aes.cryptohack.org/ctrime/encrypt/" + ((solution + c) * 2).encode('ascii').hex()).json()
        if len(r['ciphertext']) < sample:
            solution += c
            print(solution)
            if c == "}":
                print("Solution Found!", solution)
                sys.exit()
            break

#This script exploits a vulnerability in AES encryption with CTR mode by analyzing ciphertext lengths to recover a flag. It systematically appends characters to the known prefix, sends the repeated string for encryption, and observes the ciphertext length changes to deduce the correct character. The challenge demonstrates weaknesses in predictable patterns and how CTR mode can be exploited under certain conditions. 