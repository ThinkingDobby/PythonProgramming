import math

n, k = map(int, input().split())

memo = [True] * (n + 1)
memo[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if memo[i]:
        for j in range(i * 2, n + 1, i):
            memo[j] = False

primes = []
for i in range(1, n + 1):
    if memo[i]:
        primes.append(i)

cnt = 0
for i in range(1, len(primes)):
    if primes[i - 1] + primes[i] + 1 <= n:
        if memo[primes[i - 1] + primes[i] + 1]:
            cnt += 1

if cnt >= k:
    print("YES")
else:
    print("NO")