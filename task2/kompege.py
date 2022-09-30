print('a b c f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a == (b or c)) == b
            if f:
                print(a, b, c, int(f))
