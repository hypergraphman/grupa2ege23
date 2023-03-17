with open('17_5882.txt') as f:
    a = list(map(int, f.readlines()))
mn = 1_000_000
minim = 1_000_000
counter = 0
for p in range(1, len(a)):
    if (abs(a[p]) % 10 == 3) + (abs(a[p-1]) % 10 == 3) == 1:
        mn = min(mn, a[p], a[p - 1])
sm = sum(list(map(lambda x: int(x) ** 2, list(str(abs(mn))))))
for p in range(1, len(a)):
    if '3' in str(a[p]):
        if a[p] >= sm:
            counter += 1
            minim = min(minim, a[p])
print(counter)
print(minim)
