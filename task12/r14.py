for x in range(100):
    for y in range(100):
        for z in range(100):
            r1 = 2 * x + 3 * y + 6 * z
            r2 = y + z
            if r1 == 186 and r2 == 26:
                print(x + y + z + 2)
