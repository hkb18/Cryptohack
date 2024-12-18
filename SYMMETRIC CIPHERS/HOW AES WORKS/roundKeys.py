def add_round_key(s, k):
    """XORs each byte of the state with the round key."""
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. """
    return bytes([element for row in matrix for element in row])

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

result = add_round_key(state, round_key)

print(matrix2bytes(result).decode())

# This script performs the AddRoundKey step in AES, where the state matrix is XORed with the round key matrix. The result is converted into a readable plaintext string using the `matrix2bytes` function. The challenge demonstrates the role of key addition in AES rounds and its importance in the encryption and decryption process.