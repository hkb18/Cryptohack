import json
from pwn import *


token = b"\x00" * 28
address = ("socket.cryptohack.org", 13399)
conn = remote(address[0], address[1])

print(conn.recvline().decode())

token = b"\x00" * 28
resetPasswordCommand = json.dumps({"option": "reset_password", "token": token.hex()}).encode()
authCommand = json.dumps({"option": "authenticate", "password": ""}).encode()
resetCommand = json.dumps({"option": "reset_connection"}).encode()

while True:

	conn.sendline(resetPasswordCommand)
	conn.recvline().decode()

	conn.sendline(authCommand)
	ans = conn.recvline().decode()
	if "crypto" in ans:
		print(ans)
		conn.close()
		exit(0)

	conn.sendline(resetCommand)
	conn.recvline().decode()

# This script interacts with a remote server to exploit a zero-token vulnerability in a password reset mechanism. By sending a reset command with a token of all zeros and attempting authentication with an empty password, it loops through server responses until a valid flag is retrieved. The challenge demonstrates exploiting flawed authentication mechanisms and understanding network-level interactions with cryptographic services.