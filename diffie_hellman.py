import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad 

p = int(input("Enter a prime number:\np = "))
g = int(input("\nEnter a generator:\ng = "))

# Bob's private key
b = secrets.randbits(8)

# Bob's public key 
B = pow(g, b, p)

print("\nBob's public key:\nB =", B)

A = int(input("\nEnter Alice's public key:\nA = "))

s = pow(A, b, p) 
print("\nShared key:\ns =", hex(s))

# use the least-significant 128 bits of the shared key 
# as an AES-128-CBC key (encoded as 16 bytes in big endian) 
bitmask_128 = int("1"*128, 2)
aes_key = s & bitmask_128
aes_key = aes_key.to_bytes(16, byteorder="big")

iv = int(input("\nEnter the AES-128-CBC IV (hex):\nIV = "), 16)
iv = iv.to_bytes(16, byteorder="big")
ct = int(input("\nEnter the ciphertext (hex):\nct = "),16)
# rounds up to the next largest byte (takes the ceiling)
ct = ct.to_bytes((ct.bit_length() + 7) // 8, byteorder="big")

cipher = AES.new(aes_key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)

print("\nDecrypted text:\n", pt.decode())
