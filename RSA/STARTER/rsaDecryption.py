from sympy import mod_inverse

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932

# Primes from previous context
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Step 1: Compute Euler's totient φ(N)
phi_N = (p - 1) * (q - 1)

# Step 2: Compute the private key d
d = mod_inverse(e, phi_N)

# Step 3: Decrypt the ciphertext
m = pow(c, d, N)

print(f"The decrypted message is: {m}")

# This script decrypts an RSA-encrypted ciphertext c using the private key d. It computes phi(N) = (p-1)(q-1)  for the given primes p  and q , derives d as the modular inverse of e mod phi(N), and decrypts c by calculating m = c^d mod N . The challenge emphasizes the RSA decryption process and the importance of private key computations.