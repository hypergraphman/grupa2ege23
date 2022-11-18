data = tuple(map(int, open('17-344.txt').readlines()))
#print(data)
mn = min(filter(lambda x: x % 103 == 0, data))
k = 0
max_sum = 0
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if (p1 + p2) & 1 == 0 and abs(p1 - p2) % mn == 0:
        k += 1
        max_sum = max(max_sum, p1 + p2)
print(k, max_sum)
# 4 145300
