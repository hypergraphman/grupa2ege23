def alg(x):
    d100 = x % 2
    d10 = x % 3
    d1 = x % 5
    return d100 * 100 + d10 * 10 + d1


for i in range(10, 100):
    if alg(i) == 104:
        print(i)
