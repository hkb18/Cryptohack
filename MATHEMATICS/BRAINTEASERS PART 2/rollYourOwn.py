from pwn import *
import json 

io = remote('socket.cryptohack.org', 13403)
q = io.recvline().decode().strip().split(": ")[1]
q = int(q[1:-1], 0)

g = q + 1 
n = q ** 2

io.recvuntil(b"Send integers (g,n) such that pow(g,q,n) = 1: ")

to_send = dict()
to_send['g'] = hex(g)
to_send['n'] = hex(n)

io.sendline(json.dumps(to_send).encode())
pub_key = io.recvline().decode().strip().split(": ")[1]
pub_key = int(pub_key[1:-1], 0)

x = (pub_key - 1) // q 

to_send = dict()
to_send['x'] = hex(x)

io.sendline(json.dumps(to_send).encode())
io.interactive()

# This script interacts with a server to solve a cryptographic challenge based on modular arithmetic and properties of numbers. By carefully selecting g and n such that g^q mod n = 1, the script exploits the structure of q and n to derive a private value x from a public key. The challenge highlights understanding of modular exponentiation and leveraging mathematical properties to solve cryptographic problems.