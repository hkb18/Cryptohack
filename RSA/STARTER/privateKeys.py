from sympy import mod_inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Step 1: Compute Euler's totient φ(N)
phi_N = (p - 1) * (q - 1)

# Step 2: Compute the modular multiplicative inverse of e mod φ(N)
d = mod_inverse(e, phi_N)

print(f"The private key d is: {d}")

# This script encrypts a plaintext message m = 12 using RSA with a public exponent e = 65537  and modulus N = 17 c.23 . The ciphertext is computed as c = m^e mod N . The challenge demonstrates the encryption process in RSA and how the public key parameters are used to encode a message.