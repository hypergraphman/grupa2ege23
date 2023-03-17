from collections import Counter


def check(a, b, m):
    if a < m < b:
        return max(m - a, b - m)
    if a > m > b:
        return max(a - m, m - b)
    return 0


with open('17_5758.txt') as f:
    a = list(map(int, f.readlines()))

mode = Counter(a).most_common(1)[0][0]

res = []
for i in range(len(a)):
    for j in range(i + 2, len(a), 2):
        t = check(a[i], a[j], mode)
        if t:
            res.append(t)
print(len(res), max(res))
