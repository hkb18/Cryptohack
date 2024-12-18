import requests

s = requests.session()
rcount = 0
def encrypt(data):
	global rcount
	rcount += 1 
	r = s.get(f"http://aes.cryptohack.org/ecb_oracle/encrypt/{data.hex()}/")
	return(bytes.fromhex(r.json()["ciphertext"]))

def encrypt_big(data):
	MAX_SIZE = 0x10*56
	for i in range((len(data)-1)//MAX_SIZE+1):
		block = data[i*MAX_SIZE:(i+1)*MAX_SIZE]
		ct = encrypt(block)[:len(block)]
		for j in range(len(ct)//0x10):
			yield ct[j*0x10:(j+1)*0x10]


charset = list(b"etoanihsrdlucgwyfmpbkvjxqz{}_01234567890ETOANIHSRDLUCGWYFMPBKVJXQZ")
for i in range(0x100): 
	if i not in charset:
		charset.append(i)


targets = [encrypt(b"A"*(0x10-i)) for i in range(0x10)]


lengths = list(map(len, targets))
flag_len = lengths[-1] - 0x11 + lengths.index(lengths[-1])

flag = b""
for _ in range(flag_len):
	# XXX: 
	b, i = divmod(len(flag) + 1, 0x10)
	target = targets[i][b*0x10:(b+1)*0x10] 

	attempts = b""
	for c in charset:
		attempts += (b"A"*0x10+flag+bytes([c]))[-0x10:]

	for c, ct in zip(charset, encrypt_big(attempts)):
		if ct == target:
			flag += bytes([c])
			print(flag)
			break
	else:
		exit("oof")

print(f"solved in {rcount} HTTP requests!")

# This script exploits an AES encryption oracle operating in ECB mode to recover a secret flag using a byte-by-byte approach. By crafting inputs that align plaintext blocks with the secret and comparing ciphertexts, it determines the next character of the flag. The challenge demonstrates the vulnerability of ECB mode to chosen-plaintext attacks due to its deterministic and block-by-block nature.