n = int(input())
f = 1
for i in range(2, n + 1):
    f *= i
print(f)


def fact(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * fact(n - 1)


print(fact(n))