from re import *

k = 0
for line in open('24.txt').readlines():
    # if findall(r'Z*RO', line):
    #     k += 1
    #     print(line.split('RO'))
    # if match(r'Z*RO', line):
    #     k += 1
    #     print(line.split('RO'))
    try:
        if line.index('Z') < line.index('RO'):
            k += 1
            print(line.index('Z'), line.index('RO'))
            print(line)
    except:
        pass
print(k)