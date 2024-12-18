from sympy import mod_inverse


p = 9739  
a = 497   
b = 1768  


P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)


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



S = point_addition(P, P, a, p)
S = point_addition(S, Q, a, p)
S = point_addition(S, R, a, p)


x, y = S
on_curve = (y**2 - (x**3 + a * x + b)) % p == 0

print(f"Point S: {S}")
print(f"S lies on the curve: {on_curve}")

# This script performs sequential point additions on an elliptic curve defined over a finite field, verifying that the resulting point S lies on the curve. It uses modular arithmetic and the elliptic curve addition rules for both identical and distinct points. The challenge focuses on understanding elliptic curve operations and ensuring correct implementation of the addition formulas.