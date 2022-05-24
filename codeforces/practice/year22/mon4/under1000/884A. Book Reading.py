import sys

input = sys.stdin.readline

n, t = map(int, input().split())
data = list(map(int, input().split()))

chk = -1
for i in range(n):
    t -= 86400 - data[i]
    if t <= 0:
        chk = i
        break

print(chk + 1)