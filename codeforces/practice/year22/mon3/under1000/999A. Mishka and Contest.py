import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if data[i] > k:
        break
    cnt += 1

for i in data[cnt:][::-1]:
    if i > k:
        break
    cnt += 1

print(cnt)