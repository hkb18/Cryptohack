import requests, io
from PIL import Image
import numpy as np
from pwn import xor
from Crypto.Util.number import long_to_bytes, bytes_to_long

URL = "http://aes.cryptohack.org/bean_counter/encrypt"

PNG_PREFIX = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

r = requests.get(url=URL)
enc_bytes = bytes.fromhex(r.json()['encrypted'])


keystream = xor(PNG_PREFIX, enc_bytes[:16])


pt = xor(enc_bytes, keystream)

image = Image.open(io.BytesIO(pt))

image.save('bean_flag.png')

# This script decrypts an AES-encrypted image by exploiting a known plaintext prefix. It XORs the PNG file header (a known value) with the first block of encrypted bytes to derive the keystream. Using the keystream, it decrypts the entire ciphertext to reconstruct the original image and saves it as `bean_flag.png`. The challenge highlights cryptographic weaknesses when predictable plaintext is present in ECB encryption.