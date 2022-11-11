data = list(map(int, open('17-339.txt').readlines()))

t = min(filter(lambda x: x > 0 and x % 19 == 0, data))
c = 0
mx = -10**10
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    if p1 + p2 < t:
        c += 1
        mx = max(mx, p1 + p2)
print(c, abs(mx))