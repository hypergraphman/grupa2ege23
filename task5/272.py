def alg(n):
    s1 = f'{n // 2:x}'
    if n % 4:
        s2 = 'f' + s1 + 'a0'
    else:
        s2 = '15' + s1 + 'c'
    return int(s2, 16)


i = 100
while alg(i) >= 2**16:
    i -= 1
print(i)
