import math

m, n = map(int, input().split())

memo = [True] * (n + 1)
memo[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if memo[i]:
        for j in range(i * 2, n + 1, i):
            memo[j] = False

for i in range(m, n + 1):
    if memo[i]:
        print(i)

