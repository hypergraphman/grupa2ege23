f = open('26-k1.txt')
n, k = map(int, f.readline().split())

a = sorted(map(int, f.readlines()), reverse=True)
print(a[k])
print(sum(a[:k]) * 0.2)
