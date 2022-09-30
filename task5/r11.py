def alg(n):
    s1 = f'{n:b}'
    s2 = s1[1:].lstrip('0')
    if s2 == '':
        s2 = '0'
    s3 = int(s2, 2)
    return n - s3


s = set()
for i in range(500, 5000 + 1):
    s.add(alg(i))
print(len(s))
