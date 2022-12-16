def f(start, fin):
    if start == fin:
        return 1
    if start < fin:
        return 0
    return f(start - 1, fin) + f(start // 2, fin)


print(f(int('100001', 2), int('100', 2)))