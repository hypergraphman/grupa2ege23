for x in range(15):
    op1 = 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
    op2 = 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 3 * 15 + 3
    if (op1 + op2) % 14 == 0:
        print((op1 + op2) // 14, x)
