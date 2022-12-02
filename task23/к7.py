n = 29
a = [0] * (n + 1)
print(a[n])
a[2] = 1
for i in range(2, 14):
    if i + 1 <= 14:
        a[i + 1] += a[i]
    if i * 2 <= 14:
        a[i * 2] += a[i]
print(a[14])
for i in range(14, n):
    if i + 1 <= n and i + 1 != 25:
        a[i + 1] += a[i]
    if i * 2 <= n and i * 2 != 25:
        a[i * 2] += a[i]
print(a[n])
print(*a[2:])