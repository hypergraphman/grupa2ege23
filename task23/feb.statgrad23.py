def f(start, fin, cmds):
    if start == fin:
        c.add(cmds)
        return 1
    if start > fin:
        return 0
    return f(start + 1, fin, cmds + '1') + f(start + 2, fin, cmds + '2') + f(start * 2, fin, cmds + '3') + f(start * 3, fin, cmds + '4')


c = set()
print(f(1, 11, ''))
print(len(c))
k = 0
for cmd in c:
    if cmd.count('3') + cmd.count('4') == 1:
        k += 1
print(k)