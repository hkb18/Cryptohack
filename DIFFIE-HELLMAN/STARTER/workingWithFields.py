
from sympy import mod_inverse

p = 991
g = 209

d = mod_inverse(g, p)

print(d) 

# This script calculates the modular multiplicative inverse of g modulo p using SymPy. The modular inverse d is the value that satisfies 𝑔. 𝑑 ≡ 1 mod p, a fundamental operation in finite fields often used in cryptography. The challenge demonstrates understanding modular arithmetic and its applications in cryptographic computations.