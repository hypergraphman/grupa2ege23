import functools


@functools.cache
def f(start, fin):
    if start == fin:
        return 1
    if start > fin:
        return 0
    return ((f(start + 1, fin), 0)[start % 2] +
            (f(start + 2, fin), 0)[start % 2] +
            f(start * 2, fin))


print(f(1, 32))