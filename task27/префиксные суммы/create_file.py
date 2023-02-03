from random import randint

f = open('test.txt', 'w')
for _ in range(1000):
    f.write(str(randint(100, 1000)) + '\n')
f.close()