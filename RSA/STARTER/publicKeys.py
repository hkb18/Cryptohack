N = 17 * 23
ciphertext = pow(12, 65537, N)
print(ciphertext)

# This script calculates the private key d in RSA by first computing Euler's totient phi(N) = (p-1)(q-1)  for the given primes p and  q. It then computes  d, the modular inverse of e mod phi(N), which is essential for RSA decryption. The challenge highlights key generation and the mathematical foundation of RSA.