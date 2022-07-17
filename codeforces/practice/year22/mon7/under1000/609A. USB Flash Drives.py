import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
data = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
idx = -1
for i in range(n):
    if cnt >= m:
        idx = i
        break
    cnt += data[i]

print(idx if idx != -1 else n)