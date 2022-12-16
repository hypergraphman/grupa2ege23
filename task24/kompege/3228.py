lines = open('24.txt').readline().strip().replace('C', 'B').replace('AB', '1').replace('B', 'A').split('A')
print(max(map(len, lines)))
