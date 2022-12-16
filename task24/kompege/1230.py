print(max(map(len, open('24.txt').readline().strip().replace('W', '0').replace('R', '0').replace('Q', '0').split('0'))))
