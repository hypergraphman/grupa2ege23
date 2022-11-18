from math import inf

data = tuple(map(int, open('17-342.txt').readlines()))
#print(data)
mn = min(filter(lambda x: x % 37 == 0, data))
mx = max(filter(lambda x: x % 73 == 0, data))
if mx < mn:
    mx, mn = mn, mx
# print(mx, mn)
k = 0
min_sum = inf
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if (mn < p1 < mx) != (mn < p2 < mx):
        k += 1
        min_sum = min(p1 + p2, min_sum)
print(k, min_sum)