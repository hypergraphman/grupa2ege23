with open('27-a.txt') as f:
    f.readline()
    a = [int(x) for x in f.readlines()]

k = 0
for i in range(len(a)):
    for j in range(i + 18, len(a)):
        # t = a[i] + a[j]
        p = a[i] * a[j]
        if p % 2187 == 0:
            k += 1
print(k)