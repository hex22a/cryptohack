in_p1 = 5
in_a1 = 2

in_p2 = 11
in_a2 = 3

in_p3 = 17
in_a3 = 5

n = 935 # p1 * p2 * p3

def find_x(p1, a1, p2, a2, p3, a3):
    for k3 in range(0, n):
        x3 = a3 + k3 * p3
        for k2 in range(0, n):
            x2 = a2 + k2 * p2
            if x3 == x2:
                for k1 in range(0, n):
                    x1 = a1 + k1 * p1
                    if x3 == x1:
                        return x1
    return None

x = find_x(in_p1, in_a1, in_p2, in_a2, in_p3, in_a3)
print('x:', x)
print('answer', x % n)