from functools import cache


@cache
def f(n):
    if n == 1:
        return 1
    return (3 * n + 5) * f(n - 1)


def f_(n):
    f = 1
    for i in range(2, n + 1):
        f *= 3 * i + 5
    return f


for i in range(1, 2000):
    f(i)
print(f(2073)/f(2070))
print(f_(2073)/f_(2070))