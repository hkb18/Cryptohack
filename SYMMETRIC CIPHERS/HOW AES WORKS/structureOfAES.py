def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. """
    return bytes([element for row in matrix for element in row])

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix).decode()) 

# This script converts a 4x4 matrix, which represents part of the AES state, into a readable plaintext string. The `matrix2bytes` function flattens the matrix into a byte array, which is then decoded to reveal the plaintext message. The challenge highlights the structure of AES states and their transformation into plaintext during encryption or decryption.