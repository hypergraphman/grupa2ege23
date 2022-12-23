def divs(n):
    r = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return sorted(r)


for i in range(174457, 174505 + 1):
    dvs = divs(i)
    if len(dvs) == 4:
        print(dvs[1], dvs[2])