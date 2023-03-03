# mn = 10**10
# for x in range(1, 46):
#     for y in range(x, 46):
#         if 2 * x + y > 45 and x + y < mn:
#             mn = x + y
#             print(mn, x, y)
#
# print(mn)

win = 46
start = 5


def f(a, b, c, m):
    if a + b >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + i, b, c + 1, m) for i in range(1, a + 1)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)  # any, если первый ход пети был неудачный


for b in range(1, win - start):
    for m in range(1, 5):
        if f(start, b, 0, m):
            print(b, m)
            break

