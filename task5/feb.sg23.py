def f(n):
    s1 = sum(map(int, str(n)))
    s2 = n * 2 + s1 % 2
    s3 = sum(map(int, str(s2)))
    s4 = s2 * 2 + s3 % 2
    s5 = sum(map(int, str(s4)))
    s6 = s4 * 2 + s5 % 2

    return s6

print(f(25))