def f(s, c, m):
    if s >= 30:
        return c % 2 == m % 2
    # if s > 72: return c % 2 != m % 2 - с верхним ограничением
    if c == m:
        return 0
    moves = [f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)  # any, если первый ход пети был неудачный


for s in range(1, 30):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            print(s, m)
            break

