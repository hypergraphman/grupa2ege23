for a in range(1, 1000):
    is_a = True
    for k in range(1, 100):
        for n in range(1, 100):
            if not ((5 * k + 6 * n > 57) or ((k <= a) and (n < a))):
                is_a = False
                break
    if is_a:
        print(a)
        break


for a in range(1, 1000):
    if all([(5 * k + 6 * n > 57) or ((k <= a) and (n < a)) for k in range(1, 100) for n in range(1, 100)]):
        print(a)
        break