data = tuple(map(int, open('17-338.txt').readlines()))
#print(data)
mn = min(data)
k = 0
mx = 0
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if p1 % 117 == mn or p2 % 117 == mn:
        k += 1
        mx = max(p1 + p2, mx)
print(k, mx)