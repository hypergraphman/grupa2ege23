with open('27-A.txt') as f:
    f.readline()
    a = [int(x) for x in f.readlines()]

k = 0
c = a[:18]
d = [0] * 8
for i in range(18, len(a)):
    d[c[0] % 8] += 1
    k += d[(8 - a[i] % 8) % 8]
    c.pop(0)
    c.append(a[i])
print(k)

k = 0
c = a[:18]
d = [0] * 2187
for i in range(18, len(a)):
    q = c[0] % 2187
    d[q] += 1
    p = a[i] % 2187
    for j in range(len(d)):
        if j * p % 2187:
            k += d[j]
    c.pop(0)
    c.append(a[i])
print(k)
# 71405
# 2589
# [1, 3, 9, 27, 81, 243, 729, 2187]