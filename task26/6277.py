f = open('26_6277.txt')
n, v = map(int, f.readline().split())
a = [int(x) for x in f.readlines()][::-1]
cash = []
t = a.pop()
while v - t >= 0:
    cash.append(t)
    v -= t
    t = a.pop()
print(v)
cash.sort()
while a:
    find = t - v
    for i in range(len(cash)):
        if True:
            cash[i] = t
            v =
            break
    else:
        cash.pop()
    t = a.pop()
print(len(cash))