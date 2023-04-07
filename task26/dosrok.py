f = open('26 (1).txt')
k = int(f.readline())
n = int(f.readline())
cells = [0] * (k + 1)
data = []
for _ in range(n):
    s, e = map(int, f.readline().split())
    data.append((s, e))
data.sort()
last_cell = 0
amount = 0
for time in data:
    for i in range(1, len(cells)):
        if cells[i] < time[0]:
            cells[i] = time[1]
            amount += 1
            last_cell = i
            break

print(amount, last_cell)
