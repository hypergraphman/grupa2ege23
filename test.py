import itertools as it

words = set()
for word in it.permutations('ozon'):
    word = ''.join(word)
    words.add(word)

print(*words, sep='\n')
