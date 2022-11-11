from itertools import product

words = set()
for a, b, c, d in product('AE', repeat=4):
    if a <= b <= c <= d:
        word = ''.join((a, b, c, d))
        words.add(word)
print(len(words))
words = set()
for a, b, c, d in product('BCD', repeat=4):
    if a >= b >= c >= d:
        word = ''.join((a, b, c, d))
        words.add(word)
print(len(words))
words = set()
for a, b, c in product('AE', repeat=3):
    if a <= b <= c:
        word = ''.join((a, b, c))
        words.add(word)
print(len(words))
words = set()
for a, b, c in product('BCD', repeat=3):
    if a >= b >= c:
        word = ''.join((a, b, c))
        words.add(word)
print(len(words))
