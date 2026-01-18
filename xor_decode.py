from pwn import *

key1hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key12hex = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key23hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
fk123hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

key1 = bytes.fromhex(key1hex)
key12 = bytes.fromhex(key1hex)
key23 = bytes.fromhex(key23hex)
fk123 = bytes.fromhex(fk123hex)

key2 = xor(key1, key12)
key3 = xor(key23, key2)
result = xor(fk123, key1, key2, key3)

print(key2)
print(key3)
print(result)
