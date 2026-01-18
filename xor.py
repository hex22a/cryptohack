from Crypto.Util.number import *

string = 'label'
result = []

for char in string:
    xr = ord(char) ^ 13
    result.append(xr)
    print(chr(xr))

print(result)
print("".join(chr(o) for o in result))