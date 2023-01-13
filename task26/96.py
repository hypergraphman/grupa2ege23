f = open('26-96.txt')
n = int(f.readline())
d = dict()
for i in range(n):
    shir, dol = f.readline().split()
    shir = shir[:-1]
    dol = int(dol)
    if dol not in d:
        d[dol] = [1, {shir}]
    else:
        d[dol][0] += 1
        d[dol][1].add(shir)

dol = -1800
mx = 0
for key in d:
    if d[key][0] > mx:
        mx = d[key][0]
        dol = key
    elif d[key][0] == mx:
        dol = max(key, dol)

print(dol, len(d[dol][1]))