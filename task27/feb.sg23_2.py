def c3(t):
    q = 0
    while t % 3 == 0:
        q += 1
        t //= 3
    return q


with open('27-B.txt') as f:
    f.readline()
    a = [int(x) for x in f.readlines()]

k = 0
c = a[:18]
d = [[0] * 8 for _ in range(8)]
for i in range(18, len(a)):
    t = c.pop(0)
    x = c3(t)
    if x > 7:
        x = 7
    d[t % 8][x] += 1
    k += sum(d[(8 - a[i] % 8) % 8][-c3(a[i]) - 1:])
    c.append(a[i])
print(k)

# k = 0
# c = a[:18]
# d = [0] * 8
# for i in range(18, len(a)):
#     t = c.pop(0)
#     d[c3(t)] += 1
#     k += sum(d[-c3(a[i]) - 1:])
#     c.append(a[i])
# print(k)
# 71405
# 2589
# 350
# [1, 3, 9, 27, 81, 243, 729, 2187]
# [0  1  2  3   4   5    6    7]
# [   -7                  -2   -1