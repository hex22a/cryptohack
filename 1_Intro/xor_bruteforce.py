from pwn import *

hexstring = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
key = 'myXORkey'
# flag_string = 'crypto{}'

encoded = bytes.fromhex(hexstring)
print(encoded)
# bytes_flag =flag_string.encode('utf-8')
bytes_key =key.encode('utf-8')

print(xor(bytes_key, encoded))
