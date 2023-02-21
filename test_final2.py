import sys

from aes1 import AES as AES1
from aes2 import AES as AES2
from aes3 import AES as AES3
from aes4 import AES as AES4
from aes5 import AES as AES5
from aes6 import AES as AES6
from aes7 import AES as AES7
from aes8 import AES as AES8
from aes9 import AES as AES9
from aes10 import AES as AES10

print("\n\n>>>>>>>>>>  cipher text using only round 1 of AES ")
master_key = 0x3c7e155628aed2a6abf7158809cf4f3d
plaintext = 0x3243f6a8885a308d313198a2e0370734
new = AES1(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 2  ")
new = AES2(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 3  ")
new = AES3(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 4  ")
new = AES4(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 5  ")
new = AES5(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 6  ")
new = AES6(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 7  ")
new = AES7(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 8  ")
new = AES8(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using AES upto round 9  ")
#master_key = 0x3c7e155628aed2a6abf7158809cf4f3d
#plaintext = 0x3243f6a8885a308d313198a2e0370734
new = AES9(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

print("\n\n>>>>>>>>>>  cipher text using entire AES ")
#master_key = 0x3c7e155628aed2a6abf7158809cf4f3d
#plaintext = 0x3243f6a8885a308d313198a2e0370734
new = AES10(master_key)
print("plaintext = \n",plaintext)
encrypted = new.encrypt(plaintext)
print("ciphertext = \n",encrypted, "\n", 0x3925841d02dc09fbdc118597196a0b32)
decrypted = new.decrypt(encrypted)
print("original plaintext = \n", decrypted, "\n" , plaintext)

