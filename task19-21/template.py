a = [[0 for i in range(100)] for j in range(100)]
win = 83
start = 5
v2x = -2
p2x = 2
turn = v2x

turn2 = lambda x: x * 4
turn1 = lambda x: x + 1

for i in range(100):
    for j in range(100):
        if turn2(i) + j >= win or i + turn2(j) >= win:
            a[i][j] = 1
        else:
            a[i][j] = 0
# for i in range(100):
#     print(a[i])
for _ in range(100):
    for i in range(100):
        for j in range(100):
            if a[i][j] == 0:
                if (a[turn1(i)][j] > 0 and a[i][turn1(j)] > 0 and
                        a[turn2(i)][j] > 0 and a[i][turn2(j)] > 0):
                    a[i][j] = max(a[turn1(i)][j], a[i][turn1(j)],
                    a[turn2(i)][j], a[i][turn2(j)]) * (-1)
                elif (a[turn1(i)][j] < 0 or a[i][turn1(j)] < 0 or
                      a[turn2(i)][j] < 0 or a[i][turn2(j)] < 0):
                    a[i][j] = min(a[turn1(i)][j], a[i][turn1(j)],
                    a[turn2(i)][j], a[i][turn2(j)]) * (-1) + 1
for i in range(win - start):
    if a[start][i] == turn:  # сюда пишем 2 для №20 и -2 для №21
        print(i)
# for i in range(100):
#     print(a[i])
