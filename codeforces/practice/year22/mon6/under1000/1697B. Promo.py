import sys

input = sys.stdin.readline

n, q = map(int, input().split())
data = sorted(map(int, input().split()))
memo = [0 for _ in range(n)]

memo[0] = data[0]
for i in range(1, n):
    memo[i] = memo[i - 1] + data[i]

memo = [0] + memo

for _ in range(q):
    x, y = map(int, input().split())
    print(memo[n - (x - y)] - memo[n - x])