import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(input().split())

cnt = 0
for i in range(n):
    if data[i].count('4') + data[i].count('7') <= k:
        cnt += 1

print(cnt)