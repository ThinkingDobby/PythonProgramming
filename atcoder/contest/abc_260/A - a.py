import sys

input = sys.stdin.readline

data = input().rstrip()
cnt = 0
for i in data:
    if data.count(i) == 1:
        cnt += 1
        print(i)
        break
if cnt == 0:
    print(-1)