from gmpy2 import gcdext

p = 26513
q = 32321
ans=gcdext(p,q)

print(ans)


# This script computes the greatest common divisor (GCD) of two integers p and q and also finds integers x and y such that p⋅x+q⋅y=GCD(p,q) using the extended Euclidean algorithm. The challenge demonstrates understanding the relationship between GCD and modular arithmetic, crucial for cryptographic key computations and modular inverses.