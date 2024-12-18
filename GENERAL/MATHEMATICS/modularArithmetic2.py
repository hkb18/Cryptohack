def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

p = 17
result_3_17 = mod_exp(3, 17, p)
print(f"3^17 mod 17 = {result_3_17}")

result_5_17 = mod_exp(5, 17, p)
print(f"5^17 mod 17 = {result_5_17}")

result_7_16 = mod_exp(7, 16, p)
print(f"7^16 mod 17 = {result_7_16}")

base = 273246787654
exp = 65536
mod = 65537
result_large = mod_exp(base, exp, mod)
print(f"273246787654^65536 mod 65537 = {result_large}")

# This script computes modular exponentiation for various base, exponent, and modulus values using Python's `pow` function. It demonstrates the efficiency and accuracy of modular arithmetic, particularly for large numbers, which is a critical operation in cryptographic algorithms like RSA.