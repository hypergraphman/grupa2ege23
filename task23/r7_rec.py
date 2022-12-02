def f(start, fin):
    if start == 25:
        return 0
    if start == fin:
        return 1
    if start > fin:
        return 0
    return f(start + 1, fin) + f(start * 2, fin)


print(f(2, 14) * f(14, 29))