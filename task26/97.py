f = open('26-97.txt')
n = int(f.readline())
a = []
for i in range(n):
    d, s = map(int, f.readline().split())
    a.append((d, d - 2 * s - 3))
a.sort(key=lambda x: (-x[1], x[0]))
print(a)
max_pocket = []
for j in range(len(a) - 1):
    pocket = [a[j]]
    for i in range(j + 1, len(a)):
        e1 = pocket[-1][1]
        e2 = a[i][0]
        if e1 >= e2:
            pocket.append(a[i])
    if len(pocket) > len(max_pocket):
        max_pocket = pocket
print(len(max_pocket))

max_d = max_pocket[-1][0]
for e in a:
    if e[0] <= max_pocket[-2][1] and e[0] > max_d:
        max_d = e[0]
print(max_d)
# 36 106