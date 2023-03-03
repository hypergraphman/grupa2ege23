from collections import defaultdict

d = defaultdict(list)
with open('26-sg23.txt') as f:
    f.readline()
    for s in f.readlines():
        k, i = map(int, s.split())
        d[k].append(i)

for k in d.keys():
    d[k] = sorted(set(d[k]))

mx_amount = 0
mx_n = 0
for k in sorted(d.keys(), reverse=True):
    cur_len = 1
    amount = 0
    for i in range(1, len(d[k])):
        if d[k][i] - d[k][i - 1] == 1:
            cur_len += 1
            if cur_len == 3:
                amount += 1
        else:
            cur_len = 1
    if amount > mx_amount:
        mx_amount = amount
        mx_n = k
print(mx_amount, mx_n)