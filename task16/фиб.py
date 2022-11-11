from functools import cache


@cache
def f(x):
    if x <= 0:
        return -1
    if x == 1 or x == 2:
        return 1
    return f(x - 1) + f(x - 2)


# for i in range(2000):
#     f(i)
#
# print(f(2022) + f(2023))

n = int(input())
prev = 1
cur = 1
for i in range(2, n):
    prev, cur = cur, prev + cur
print(cur)