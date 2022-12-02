n = 20
a = [0] * (n + 1)
print(a[n])
a[1] = 1
for i in range(1, 10):
    if i + 1 <= 10:
        a[i + 1] += a[i]
    if i * 2 <= 10:
        a[i * 2] += a[i]
print(a[10])
for i in range(10, n):
    if i + 1 <= n:
        a[i + 1] += a[i]
    if i * 2 <= n:
        a[i * 2] += a[i]
print(a[n])
