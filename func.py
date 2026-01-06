n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sqrt_val = d**0.5
    sol1 = (-b + sqrt_val) / (2 * a)
    sol2 = (-b - sqrt_val) / (2 * a)
    return sol1, sol2
