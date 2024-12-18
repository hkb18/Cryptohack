p = 9739  
a = 497   
b = 1768  


Px, Py = 8045, 6936


Qx = Px
Qy = (-Py) % p

print(f"The negated point Q is: ({Qx}, {Qy})")

#  This script computes the negation of a point P on an elliptic curve over a finite field. It calculates Q=(Px,−Pymodp), ensuring that P+Q=O (the identity element). The challenge emphasizes understanding point negation and its role in elliptic curve arithmetic.