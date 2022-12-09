import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data += data
data += [2]
cnt = 0
mv = 0
for i in range(1, n * 2 + 1):
    if data[i - 1] != data[i]:
        if data[i - 1] == 1:
            mv = max(mv, cnt)
        cnt = 0
    cnt += 1

print(mv)
