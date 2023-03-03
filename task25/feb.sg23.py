from re import fullmatch
for i in range(4173, 10**10, 4173):
    if fullmatch(r'1\d7246\d*1', str(i)):
        print(i)