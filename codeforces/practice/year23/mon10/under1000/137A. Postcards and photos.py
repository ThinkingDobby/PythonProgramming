import sys

input = sys.stdin.readline

data = input().rstrip()
data = '?' + data

cnt = 0
now = 0
for i in range(1, len(data)):
    if data[i - 1] != data[i]:
        now = 1
        cnt += 1
    else:
        now += 1

    if now > 5:
        now = 1
        cnt += 1


print(cnt)