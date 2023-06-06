def extended_euclidean_algorithm(a, m):
    if m == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclidean_algorithm(m, a % m)
    x = y1
    y = x1 - (a // m) * y1
    return gcd, x, y

def modular_multiplicative_inverse(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        raise ValueError("Modular multiplicative inverse does not exist.")
    return (x % m + m) % m


a = 7
m = 26

mod_inverse = modular_multiplicative_inverse(a, m)
print("Modular Multiplicative Inverse:", mod_inverse)
