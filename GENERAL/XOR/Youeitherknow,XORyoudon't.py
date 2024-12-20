from binascii import unhexlify

def brute(input, key):
    if len(input) != len(key):
        return "Failed!"

    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(data)
print("[-] CIPHER: {}".format(cipher))

# First Step
key_part = brute(cipher[:7], "crypto{".encode())
print("[-] PARTIAL KEY FOUND: {}".format(key_part))

# Second Step
key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key))/len(key))
key += key[:((len(cipher) - len(key))%len(key))]
print("[-] Decoding using KEY: {}".format(key))

plain = brute(cipher, key)
print("\n[*] FLAG: {}".format(plain))

# This script attempts to decrypt a ciphertext encrypted using a repeating XOR key. It first derives part of the key by XORing the initial ciphertext bytes with a known plaintext prefix, "crypto{". The complete key is reconstructed by repeating and extending the partial key to match the ciphertext length, enabling decryption of the entire message. The challenge emphasizes repeating XOR encryption analysis and partial key recovery techniques.