import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = set([input().rstrip() for _ in range(n)])
data = [input().rstrip() for _ in range(m)]

cnt = 0
for i in data:
    if i in memo:
        cnt += 1

print(cnt)
