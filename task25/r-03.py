def divs(n):
    r = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return sorted(r)


left = int('7' * 8)
right = int('8' * 8)
a = []
for p in range(3, 131):
    if len(divs(p)) == 2:
        for x in range(27):
            if left <= 2**x * p**4 <= right:
                a.append((2**x * p**4, p))
print(*sorted(a), sep='\n')
