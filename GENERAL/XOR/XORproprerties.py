from Cryptodome.Util.number import *
KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ KEY1
KEY3 = KEY2 ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ KEY1 ^ KEY3 ^ KEY2
print(long_to_bytes(FLAG))


# This script demonstrates the use of XOR properties to sequentially derive keys and decrypt a flag. By leveraging the associative and reversible nature of XOR, it calculates the flag by combining three keys and the encrypted flag using bitwise operations. The challenge emphasizes understanding XOR operations and their application in cryptographic key recovery and decryption.