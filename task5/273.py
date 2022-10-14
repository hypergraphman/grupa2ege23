def alg(n):
    s1 = f'{n:b}'
    if n % 2:
        s2 = '1' + s1 + '0'
    else:
        s2 = '11' + s1 + '11'
    return int(s2, 2)


a = set()
for i in range(1, 100000):
    if alg(i) < 126:
        a.add(alg(i))
print(max(a))

