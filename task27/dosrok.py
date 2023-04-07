f = open('27.txt')
k = int(f.readline())
n = int(f.readline())
a = []
for _ in range(k):
    a.append(int(f.readline()))
mx_left = 0
mx = 0
for i in range(n - k):
    x = int(f.readline())
    mx_left = max(mx_left, a.pop(0))
    # mx_left = max(mx_left, a[i % k])
    mx = max(mx, mx_left + x)
    a.append(x)
    # a[i % k] = x
print(mx)