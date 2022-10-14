from itertools import product

alf = 'aezymu'
p = [el * 2 for el in alf]
c = 0
for i, word in enumerate(product(alf, repeat=5), start=1):
    word = ''.join(word)
    if i % 2 == 0 and all([x not in word for x in p]):
        c += 1
print(c)