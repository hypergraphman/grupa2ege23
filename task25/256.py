# from re import fullmatch
#
# for i in range(92, 10**8, 92):
#     if fullmatch(r'12[02468]4[13579]6\d8', str(i)):
#         print(i, i // 92)
#
# 12043628 130909
# 12049608 130974
# 12445668 135279
# 12641628 137409
# 12647608 137474

# 01234567
# 12X4Y6A8
for i in range(92, 10**8, 92):
    t = str(i)
    if (len(t) == 8 and '12' == t[:2] and t[3] == '4' and '6' == t[5] and
       t[7] == '8' and t[2] in '02468' and t[4] in '13579' and t[6] in '0123456789'):
        print(i, i // 92)