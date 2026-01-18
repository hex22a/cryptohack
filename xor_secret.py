from pwn import *

hexstring = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

encoded = bytes.fromhex(hexstring)

for i in range(0xff):
    print(xor(encoded, i))
