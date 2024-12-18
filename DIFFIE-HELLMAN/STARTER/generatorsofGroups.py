from sympy.ntheory import is_primitive_root

p = 28151
g = 2

while not is_primitive_root(g, p):
    g += 1

print(g)

# This script identifies the smallest primitive root modulo a given prime 𝑝, starting with 𝑔 =2. It incrementally checks each g until it finds one that satisfies the properties of a primitive root, making it useful for cryptographic protocols like Diffie-Hellman. The challenge emphasizes understanding group generators and their significance in modular arithmetic.