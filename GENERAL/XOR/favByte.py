hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

encoded_bytes = bytes.fromhex(hex_string)

# Function to XOR the bytes with a given key
def xor_bytes(key):
    return bytes([byte ^ key for byte in encoded_bytes])

# Function to check if the result contains the word 'crypto'
def contains_crypto(text):
    return b'crypto' in text

# Try XORing with all possible bytes and check if result contains 'crypto'
for key in range(256):
    decoded_bytes = xor_bytes(key)
    if contains_crypto(decoded_bytes):
        print(f"Key: {key}, Decoded Text: {decoded_bytes.decode()}")

# This script attempts to decode a hex-encoded string by XORing it with all possible single-byte keys (0–255) to find the key that reveals a plaintext containing the word "crypto." It systematically tests each key and checks the result for the target substring. The challenge highlights the use of XOR in cryptanalysis and brute-force techniques for ciphertext decoding.        