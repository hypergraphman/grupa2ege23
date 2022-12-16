def f(start, fin, i):
    if start == fin:
        if i == 7:
            return 1
        else:
            return 0
    if start > fin:
        return 0
    return f(start + 1, fin, i + 1) + f(start + 4, fin, i + 1) + f(start * 2, fin, i + 1)


print(f(3, 27, 0))