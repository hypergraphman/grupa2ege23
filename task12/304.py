for x in range(100):
    for y in range(100):
        for z in range(100):
            r1 = 3 * x + y + 7 * z
            r2 = x + 3 * z
            r3 = 2 * x + y + 6 * z
            if r1 == 104 and r2 == 39 and r3 == 83:
                print(x + y + z + 2)
