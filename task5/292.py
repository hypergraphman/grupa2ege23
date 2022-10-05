def alg(n):
    s1 = f'{n:b}'
    if s1.count('1') % 2 == 0:
        s2 = '10' + s1[2:] + '0'
    else:
        s2 = '11' + s1[2:] + '1'
    return int(s2, 2)


i = 100
while alg(i) >= 35:
    i -= 1
print(i)
