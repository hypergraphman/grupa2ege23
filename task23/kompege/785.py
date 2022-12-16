def f(start, fin):
    if start == fin:
        return 1
    if start > fin:
        return 0
    return f(start + 1, fin) + f(start + start + 1 + start % 2, fin) + f(start * 2, fin)


print(f(3, 25) * f(25, 75))