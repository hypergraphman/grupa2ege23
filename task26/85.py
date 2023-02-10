from collections import defaultdict


FREE = 100
H = 500
d = defaultdict(list)
# with open('test.txt') as f:
with open('26-85.txt') as f:
    n = int(f.readline())
    for line in f.readlines():
        row, cell, city = map(int, line.split())
        if cell == 0:
            print(row)
        d[row].append(cell * (-1)**city)
# print(d)
# print(sorted(d.keys(), key=lambda x: -x))
for r in sorted(d.keys(), key=lambda x: -x):
    row = sorted(d[r], key=lambda x: abs(x))
    if len(list(filter(lambda x: x > 0, d[r]))) >= H:
        for c1, c2 in zip(row, row[1:]):
            if c1 < 0 and c2 < 0 and c1 - c2 - 1 == FREE:
                print(r, len(list(filter(lambda x: x <= 0, d[r]))))
                print(row)
