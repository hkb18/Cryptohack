from Crypto.PublicKey import RSA

with open('CryptoHack\privacy-enhanced mail\privacy_enhanced_mail.pem','r') as key_file:
    key = RSA.importKey(key_file.read()).d
    print(key)

# This script extracts the private exponent d from an RSA private key stored in PEM format using the `Crypto.PublicKey.RSA` library. The challenge focuses on parsing cryptographic key files and understanding their structures for RSA cryptography.