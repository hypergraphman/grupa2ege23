F = open("27_B.txt")
N = int(F.readline())
K = 43
tailSum = [0] + [None] * (K - 1)
tailLen = [0] * K
maxSum, minLen = 0, 0
totalSum = 0
for i in range(1, N + 1):
    x = int(F.readline())
    totalSum += x
    r = totalSum % K
    if tailSum[r] != None:
        curSum = totalSum - tailSum[r]
        curLen = i - tailLen[r]
        if curSum > maxSum or \
                (curSum == maxSum and curLen < minLen):
            maxSum = curSum
            minLen = curLen
    else:
        tailSum[r] = totalSum
        tailLen[r] = i
F.close()
print(minLen)
