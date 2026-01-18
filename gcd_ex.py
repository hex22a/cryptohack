a = 32321
b = 26513

# a > b

def gcdex_r(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, u, v = gcdex_r(b, a % b)
        return d, v, u - v * (a // b)

def gcdex(a, b, u, v):
    if a % b == 0:
        u = 0
        v = 1
        return b

    q0 = a // b
    u0 = 1
    v0 = -q0
    r0 = a - b * q0

    if b % r0 == 0:
        u = u0
        v = v0
        return r0

    q1 = b // r0
    r1 = b - r0 * q1
    u1 = -q1
    v1 = 1 + q0 * q1

    while r0 % r1 != 0:
        q = r0 // r1

        u2 = u0 - u1 * q
        v2 = v0 - v1 * q
        r2 = r0 - r1 * q

        u0 = u1
        v0 = v1
        r0 = r1

        u1 = u2
        v1 = v2
        r1 = r2

    u = u1
    v = v1

    return r1, u, v

print(gcdex(a, b, 0, 1))
print(gcdex_r(a, b))