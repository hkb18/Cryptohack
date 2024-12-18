p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Calculate Euler's totient φ(N)
phi_N = (p - 1) * (q - 1)

print(phi_N)

# This script calculates Euler's totient phi(N) for a given RSA modulus N = p c. q, where p and q are prime numbers. It computes phi(N) = (p-1)(q-1), which is essential in RSA for determining the private key d. The challenge highlights the calculation of phi(N) as a foundational step in RSA cryptography.