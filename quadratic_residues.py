p = 29
ints = [14, 6, 11]


# print(pow(12, 2) % p)
# print(pow(11, 2, p))

for a in range(1, p - 1):
    if pow(a, 2, p) in ints:
        print('\n>>>>')
        print(a)
        print(pow(a, 2, p))
