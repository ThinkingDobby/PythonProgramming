import sys

input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))
queries = list(map(int, input().split()))

memo = [-1] * 50
for i in range(n - 1, -1, -1):
    memo[data[i] - 1] = i + 1

for i in queries:
    now = memo[i - 1]
    for j in range(50):
        if memo[j] != -1 and memo[j] < now:
            memo[j] += 1
    print(now, end=' ')
    memo[i - 1] = 1