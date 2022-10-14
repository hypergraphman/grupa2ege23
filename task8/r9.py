from itertools import permutations, product

words = set()
for word in permutations('vualy'):
    word = ''.join(word)
    if not ('ya' in word or 'yu' in word or
            word[0] == 'y'):
        words.add(word)
print(len(words))
