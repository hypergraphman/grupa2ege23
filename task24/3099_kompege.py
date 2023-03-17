from collections import Counter


with open('24_3099.txt') as f:
    a = f.readline()
print(len(a))
print(Counter(a))