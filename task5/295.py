def alg(n, m):
    sn = sum(map(int, f'{n:b}'))**2
    sm = sum(map(int, f'{m:b}')) ** 2
    return sn - sm


a = set()
for i in range(1000):
    for j in range(1000):
        if alg(i, j) == 33:
            a.add(i + j)
print(min(a))
