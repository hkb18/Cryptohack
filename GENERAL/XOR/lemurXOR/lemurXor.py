from PIL import Image, ImageChops

im1 = Image.open("CryptoHack/lemurXOR/lemur.png")
im2 = Image.open("CryptoHack/lemurXOR/flag.png")

im3 = ImageChops.difference(im1,im2)


im3.show()
im3.save("CryptoHack/lemurXOR/final.png")

# This script compares two images using XOR-like pixel operations via `ImageChops.difference`, revealing differences between them. The resulting image highlights discrepancies, potentially uncovering a hidden message or embedded information. The challenge focuses on applying visual cryptography concepts and analyzing pixel-level data for steganographic clues.