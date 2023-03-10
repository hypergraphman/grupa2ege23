
for a in range(0, 1000):
    if all([((x&35!=0) or (x&22!=0)) <= ((x&15==0) <= (x&a!=0)) for x in range(0, 1000)]):
        print(a)