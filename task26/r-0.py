for i in range(1, 20 + 1):
    with open(f'26-{i}.txt') as f:
        v, n = map(int, f.readline().split())
        data = sorted([int(x) for x in f.readlines()])

    k = 0
    while v - data[k] >= 0:
        v -= data[k]
        k += 1
    print(i, k, end=' ')
    v += data[k - 1]
    while k < n and v - data[k] >= 0:
        k += 1
    print(data[k - 1])
