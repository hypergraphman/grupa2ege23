with open('17.txt') as f:
    a = [int(x) for x in f.readlines()]
m = min(filter(lambda x: abs(x) % 10 == 3, a)) ** 2
t = []
for p1, p2 in zip(a, a[1:]):
    if abs(p1) % 10 == abs(p2) % 10 and (p1 % 3 == 0 and p2 % 3 != 0 or
                                         p1 % 3 != 0 and p2 % 3 == 0) and p1 ** 2 + p2 ** 2 <= m:
        t.append(p1 ** 2 + p2 ** 2)
print(len(t), max(t))
