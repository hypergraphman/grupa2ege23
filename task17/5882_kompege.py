with open('17_5882.txt') as f:
    a = list(map(int, f.readlines()))

t = []
for p1, p2 in zip(a, a[1:]):
    if (abs(p1) % 10 == 3) != (abs(p2) % 10 == 3):
        t.append(min(p1, p2))
mn = min(t)
s = 0
for c in str(abs(mn)):
    s += int(c)**2
print(s)

res = []
for p in a:
    if '3' in str(p) and p >= s:
        res.append(p)
print(len(res), min(res))