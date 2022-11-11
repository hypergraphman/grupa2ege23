def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n // 3)
    return n + f(n + 3)


for i in range(3, 1000 + 1, 3):
    try:
        if f(i) > 100:
            print(i)
            break
    except Exception:
        pass
