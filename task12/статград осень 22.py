for x in range(55):
    for y in range(55):
        for z in range(55):
            for w in range(55):
                if y + 2 * w == 40 and x + 2 * z == 52 and x * 2 + z == y * 2 + w:
                    print(x + 2 * z)
                    print(x, y, z, w)



# from itertools import permutations
#
# n = 4
# line = '1' * n + '2' * n
# s = set()
# for r in permutations(line):
#     s.add(''.join(r))
#
#
# for l in s:
#     # print(l, end=' ')
#     t = l
#     l = '0' + l + '0'
#     while '00' not in l:
#         l = l.replace('011', '20', 1)
#         l = l.replace('022', '10', 1)
#         l = l.replace('01', '220', 1)
#         l = l.replace('02', '110', 1)
#     # print(l[:-2], l.count('1'), l.count('2'))
#     if l.count('1') < l.count('2'):
#         print(t, l[:-2], l.count('1'), l.count('2'))