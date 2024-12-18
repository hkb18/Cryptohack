from sympy import mod_inverse


p = 9739  
a = 497  
b = 1768  


P = (2339, 2213)

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



Q = scalar_multiplication(P, 7863, a, p)


x, y = Q
on_curve = (y**2 - (x**3 + a * x + b)) % p == 0

print(f"Point Q: {Q}")
print(f"Q lies on the curve: {on_curve}")

# This script performs scalar multiplication on an elliptic curve point P using the double-and-add algorithm, calculating [n]P. It verifies that the resulting point Q lies on the curve by checking the elliptic curve equation. The challenge highlights efficient computation of scalar multiplication and its significance in elliptic curve cryptography.