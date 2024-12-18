a = 3  
p = 13  

mod_inverse = pow(a, p - 2, p)

print(f"The modular inverse of {a} mod {p} is {mod_inverse}")

# This script calculates the modular inverse of a modulo p using Fermat's Little Theorem, where 𝑎^−1 ≡ 𝑎^𝑝−2 mod p . The challenge highlights modular inversion, an essential concept in cryptography for solving equations in finite fields.