from functools import lru_cache


@lru_cache(None)
def divs(n):
    r = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return r


with open('17_4329.txt') as f:
    a = list(map(int, f.readlines()))

mx = (divs(a[0]), a[0])
for el in a:
    t = (divs(el), el)
    if len(t[0]) > len(mx[0]):
        mx = t

res = []
for p1, p2 in zip(a, a[1:]):
    if len(divs(p1) & mx[0]) >= 3 and len(divs(p2) & mx[0]) >= 3:
        res.append(len(divs(p1) & divs(p2)))
print(len(res), max(res))