import hashlib
from sympy import mod_inverse


p = 9739  
a = 497   
b = 1768  


G = (1804, 5368)


Q_A = (815, 3190)


n_B = 1829


def point_addition(P, Q, a, p):
    """Adds two points P and Q on the elliptic curve."""
    if P == "O":
        return Q
    if Q == "O":
        return P
    if P[0] == Q[0] and (P[1] + Q[1]) % p == 0:
        return "O"

    if P == Q:
        
        num = (3 * P[0]**2 + a) % p
        denom = mod_inverse(2 * P[1], p)
    else:
        
        num = (Q[1] - P[1]) % p
        denom = mod_inverse(Q[0] - P[0], p)

    lam = (num * denom) % p

    x_r = (lam**2 - P[0] - Q[0]) % p
    y_r = (lam * (P[0] - x_r) - P[1]) % p

    return (x_r, y_r)


def scalar_multiplication(P, n, a, p):
    """Computes [n]P using the double and add algorithm."""
    R = "O"  
    Q = P    

    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p) 
        Q = point_addition(Q, Q, a, p)      
        n //= 2

    return R



shared_secret = scalar_multiplication(Q_A, n_B, a, p)


x_coord = shared_secret[0]
key = hashlib.sha1(str(x_coord).encode()).hexdigest()

print(f"SHA-1 Hash (Key): {key}")

# This script implements elliptic curve cryptography (ECC) to compute a shared secret using scalar multiplication on a defined elliptic curve. It applies point addition and the double-and-add method to calculate the scalar product and derives a symmetric key by hashing the \( x \)-coordinate of the shared secret. The challenge focuses on understanding ECC operations and their use in cryptographic key exchanges.