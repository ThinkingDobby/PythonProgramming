import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(input().rstrip())
scores = list(map(int, input().split()))

ans = 0
for i in range(m):
    ans += scores[i] * max(collections.Counter([data[j][i] for j in range(n)]).values())

print(ans)