import sys

input = sys.stdin.readline

n, m, t = map(int, input().split())

data = list(map(int, input().split()))
bonus = {}

for _ in range(m):
    x, y = map(int, input().split())
    bonus[x - 1] = y

ans = True
for i in range(n - 1):
    if i in bonus:
        t += bonus[i]
    if t <= data[i]:
        ans = False
        break
    t -= data[i]

print("Yes" if ans else "No")