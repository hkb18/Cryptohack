
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  
    return x % m


def chinese_remainder_theorem(a, n):
    N = 1
    for ni in n:
        N *= ni  
    
    x = 0
    for ai, ni in zip(a, n):
        Ni = N // ni  
        Mi = mod_inverse(Ni, ni)  
        x += ai * Ni * Mi
    
    return x % N


a = [2, 3, 5]  
n = [5, 11, 17]  


x = chinese_remainder_theorem(a, n)
print(x)

# This script implements the Chinese Remainder Theorem (CRT) to solve a system of modular equations x equiv a_i pmod{n_i} . It calculates the product of all moduli, determines modular inverses, and combines the results to find the unique solution modulo N, where N is the product of all  n_i . The challenge focuses on understanding CRT and its applications in modular arithmetic and cryptographic algorithms.