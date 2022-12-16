def f(start, fin):
    if start == fin:
        return 1
    if start > fin:
        return 0
    return f(start + 4, fin) + f(start * 2 + 1, fin) + f(start + 10, fin)


print(f(2, 27))