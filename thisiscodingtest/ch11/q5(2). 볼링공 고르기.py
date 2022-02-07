n, m = map(int, input().split())
data = list(map(int, input().split()))
memo = [0] * (m + 1)
for i in data:
    memo[i] += 1

s = 0
for i in range(1, m):
    s += memo[i] * sum(memo[i + 1:])

print(s)