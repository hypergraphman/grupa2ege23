f = open('27_B.txt')
n = int(f.readline())
a = list(map(int, f.readlines()))
count = 0
for i in range(n):
    if a[i] % 43 != 0:
        print(i, a[i] % 43)
        count += 1
print(count)