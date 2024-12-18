import requests

url_base = 'http://aes.cryptohack.org/lazy_cbc'

BLOCK_SIZE = 16
ZERO = b'\0' * 16

def hack():
  response = requests.get(url="%s/encrypt/%s" % (url_base, ZERO.hex())).json()


  ciphertext = bytes.fromhex(response['ciphertext'])


  ciphertext = ZERO + ciphertext
  response = requests.get(url="%s/receive/%s" % (url_base, ciphertext.hex())).json()


  plaintext = bytes.fromhex(response['error'][len('Invalid plaintext: '):])
  key = plaintext[BLOCK_SIZE:] # K is the second block

  response = requests.get(url="%s/get_flag/%s" % (url_base, key.hex())).json()
  return bytes.fromhex(response['plaintext']).decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)

# This script exploits a vulnerability in a CBC encryption service by prepending a block of zeros to the ciphertext. By analyzing the server's error response, it extracts the encryption key embedded in the plaintext of the modified ciphertext. The challenge demonstrates how improper handling of CBC mode and predictable plaintexts can lead to key recovery and full compromise of the encryption scheme.