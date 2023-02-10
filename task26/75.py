# with open('test.txt') as f:
with open('26-75.txt') as f:
    n = int(f.readline())
    a = []
    for line in f.readlines():
        t = line.split()
        a.append(int(t[0]))
        a.append(-int(t[1]))
a.sort(key=lambda x: abs(x))
# print(a)
k = 0
max_k = 0
s = 0
at_least_one = None
for e in a:
    if e > 0:
        if not at_least_one:
            at_least_one = e
        k += 1
        max_k = max(k, max_k)
    else:
        k -= 1
        if k == 0:
            s += abs(e) - at_least_one
            at_least_one = None
print(max_k, s)