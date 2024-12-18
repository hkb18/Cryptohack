import requests
from Crypto.Util.Padding import unpad

def encrypt_flag(key):
    res = requests.get(f"http://aes.cryptohack.org/triple_des/encrypt_flag/{key.hex()}")
    return bytes.fromhex(res.json()['ciphertext'])

def encrypt(key, plaintext):
    res = requests.get(f"http://aes.cryptohack.org/triple_des/encrypt/{key.hex()}/{plaintext.hex()}/")
    return bytes.fromhex(res.json()['ciphertext'])


key1 = b"\x01\x01\x01\x01\x01\x01\x01\x01"
key2 = b"\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe"


key = key1+key2

encrypted_flag = encrypt_flag(key)
flag = unpad(encrypt(key, encrypted_flag), 8)
print(flag.decode())

# This script decrypts a Triple DES-encrypted flag by leveraging a known key structure. It constructs a composite key from two DES keys text{key1} and text{key2} , retrieves the encrypted flag, and decrypts it using the same composite key. The challenge demonstrates understanding the Triple DES encryption scheme and how combining multiple keys impacts the encryption and decryption process.