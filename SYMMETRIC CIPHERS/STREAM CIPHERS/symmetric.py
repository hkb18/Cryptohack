import requests

url_base = 'http://aes.cryptohack.org/symmetry'

BLOCK_SIZE = 16

def hack():
  response = requests.get(url="%s/encrypt_flag/" % url_base).json()
  ciphertext = bytes.fromhex(response['ciphertext'])

 
  iv, ciphertext = ciphertext[:BLOCK_SIZE], ciphertext[BLOCK_SIZE:]


  response = requests.get(url="%s/encrypt/%s/%s" % (url_base, ciphertext.hex(), iv.hex())).json()
  plaintext = bytes.fromhex(response['ciphertext'])
  return plaintext.decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)

# This script exploits a vulnerability in a symmetric encryption setup by reusing the ciphertext and IV to decrypt the plaintext. It takes advantage of the malleability of CBC mode when encryption endpoints are exposed, flipping the roles of ciphertext and IV. The challenge demonstrates understanding weaknesses in symmetric encryption protocols and how improper API usage can lead to data leakage.