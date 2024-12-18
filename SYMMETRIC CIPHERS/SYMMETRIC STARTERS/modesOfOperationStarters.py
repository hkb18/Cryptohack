import requests

url = "https://aes.cryptohack.org/block_cipher_starter/"
ciphertext = requests.get(url + "encrypt_flag/").json()["ciphertext"]
plaintext_hex = requests.get(url + "decrypt/" + ciphertext ).json().get("plaintext")

print(bytes.fromhex(plaintext_hex).decode())

# This script interacts with an API to decrypt an AES-encrypted ciphertext. It retrieves the ciphertext via an API call, sends it back for decryption, and converts the returned plaintext from hex to readable text. The challenge highlights understanding AES decryption and using external services to analyze cryptographic operations.