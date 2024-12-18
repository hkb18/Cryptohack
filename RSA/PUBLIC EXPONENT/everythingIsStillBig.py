import gmpy2
from Crypto.Util.number import long_to_bytes


def t_cf(n, d):  
    res = []
    while d:
        res.append(n // d)
        n, d = d, n % d
    return res


def cf(sub_res):  
    n, d = 1, 0
    for i in sub_res[::-1]:  
        d, n = n, i * n + d
    return d, n


def list_fraction(x, y):  
    res = t_cf(x, y)
    res = list(map(cf, (res[0:i] for i in range(1, len(res)))))  
    return res


def get_pq(a, b, c):  
    par = gmpy2.isqrt(b * b - 4 * a * c)  
    x1, x2 = (-b + par) // (2 * a), (-b - par) // (2 * a)
    return x1, x2


def wienerAttack(e, n):
    for (d, k) in list_fraction(e, n): 
        if k == 0: 
            continue
        if (e * d - 1) % k != 0:  
            continue

        phi = (e * d - 1) // k 
        px, qy = get_pq(1, n - phi + 1, n)

        if px * qy == n:
            p, q = abs(int(px)), abs(int(qy))  
            d = gmpy2.invert(e, (p - 1) * (q - 1))  
            return d
    print("Failed to solve for d")
n = 0xb12746657c720a434861e9a4828b3c89a6b8d4a1bd921054e48d47124dbcc9cfcdcc39261c5e93817c167db818081613f57729e0039875c72a5ae1f0bc5ef7c933880c2ad528adbc9b1430003a491e460917b34c4590977df47772fab1ee0ab251f94065ab3004893fe1b2958008848b0124f22c4e75f60ed3889fb62e5ef4dcc247a3d6e23072641e62566cd96ee8114b227b8f498f9a578fc6f687d07acdbb523b6029c5bbeecd5efaf4c4d35304e5e6b5b95db0e89299529eb953f52ca3247d4cd03a15939e7d638b168fd00a1cb5b0cc5c2cc98175c1ad0b959c2ab2f17f917c0ccee8c3fe589b4cb441e817f75e575fc96a4fe7bfea897f57692b050d2b
e = 0x9d0637faa46281b533e83cc37e1cf5626bd33f712cc1948622f10ec26f766fb37b9cd6c7a6e4b2c03bce0dd70d5a3a28b6b0c941d8792bc6a870568790ebcd30f40277af59e0fd3141e272c48f8e33592965997c7d93006c27bf3a2b8fb71831dfa939c0ba2c7569dd1b660efc6c8966e674fbe6e051811d92a802c789d895f356ceec9722d5a7b617d21b8aa42dd6a45de721953939a5a81b8dffc9490acd4f60b0c0475883ff7e2ab50b39b2deeedaefefffc52ae2e03f72756d9b4f7b6bd85b1a6764b31312bc375a2298b78b0263d492205d2a5aa7a227abaf41ab4ea8ce0e75728a5177fe90ace36fdc5dba53317bbf90e60a6f2311bb333bf55ba3245f
c = 0xa3bce6e2e677d7855a1a7819eb1879779d1e1eefa21a1a6e205c8b46fdc020a2487fdd07dbae99274204fadda2ba69af73627bdddcb2c403118f507bca03cb0bad7a8cd03f70defc31fa904d71230aab98a10e155bf207da1b1cac1503f48cab3758024cc6e62afe99767e9e4c151b75f60d8f7989c152fdf4ff4b95ceed9a7065f38c68dee4dd0da503650d3246d463f504b36e1d6fafabb35d2390ecf0419b2bb67c4c647fb38511b34eb494d9289c872203fa70f4084d2fa2367a63a8881b74cc38730ad7584328de6a7d92e4ca18098a15119baee91237cea24975bdfc19bdbce7c1559899a88125935584cd37c8dd31f3f2b4517eefae84e7e588344fa5

d = wienerAttack(e, n)
m = pow(c,d,n)
print(long_to_bytes(m))

# This script executes Wiener's attack on an RSA system to decrypt a ciphertext c. By leveraging the vulnerability of small private exponents d , it uses continued fraction approximations of e/n to compute candidate values for d, checks their validity, and calculates the plaintext m if successful. The challenge emphasizes the risks of using small d in RSA, which can compromise the encryption's security.