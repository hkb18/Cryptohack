from sympy import mod_inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


p = 9739
a = 497
b = 1768
G = (1804, 5368)
n_B = 6534
x_QA = 4726


iv = "cd9da9f1c60925922377ea952afc212c"
ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"


def mod_sqrt(x, p):
    return pow(x, (p + 1) // 4, p)


rhs = (x_QA**3 + a * x_QA + b) % p
y_pos = mod_sqrt(rhs, p)
y_neg = (-y_pos) % p


Q_A1 = (x_QA, y_pos)
Q_A2 = (x_QA, y_neg)


def point_add(P, Q, p):
    if P == "O":
        return Q
    if Q == "O":
        return P
    if P[0] == Q[0] and P[1] == (-Q[1] % p):
        return "O"

    if P == Q:
        
        m = (3 * P[0]**2 + a) * mod_inverse(2 * P[1], p) % p
    else:
     
        m = (Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p) % p

    x_r = (m**2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)

def scalar_mult(k, P, p):
    R = "O"
    N = P
    while k:
        if k & 1:
            R = point_add(R, N, p)
        N = point_add(N, N, p)
        k >>= 1
    return R


S1 = scalar_mult(n_B, Q_A1, p)[0]
S2 = scalar_mult(n_B, Q_A2, p)[0]


def decrypt_flag(shared_secret, iv, ciphertext):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, 16).decode('ascii')

flag = decrypt_flag(S1, iv, ciphertext)
print("Decrypted Flag:", flag)

# This script performs an elliptic curve Diffie-Hellman key exchange using the \( x \)-coordinate of points derived from scalar multiplication to compute two potential shared secrets. It then uses one shared secret to derive an AES key for decrypting a ciphertext in CBC mode. The challenge combines efficient elliptic curve operations, modular arithmetic, and symmetric key decryption to highlight cryptographic precision and error handling.