from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    # alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alf = digits + ascii_uppercase
    while n != 0:
        d = n % p
        r = alf[d] + r
        n //= p
    return r


print(n_to_p(100, 2))  # 1100100
print(n_to_p(255, 16))  # FF
print(n_to_p(194, 5))  # 1234
