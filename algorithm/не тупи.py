from string import digits, ascii_uppercase


def n_to_p(n, p):
    # digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit = digits + ascii_uppercase
    r = ''
    while n != 0:
        d = n % p
        r = digit[d] + r
        n //= p
    return r


print(n_to_p(255, 16))
print(n_to_p(100, 2))
print(n_to_p(194, 5))
