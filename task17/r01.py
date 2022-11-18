k = 0
mx = 0
for n in range(1017, 7937 + 1, 3):
    if n % 7 and n % 17 and n % 19 and n % 27:
        k += 1
        mx = n
print(k, mx)
