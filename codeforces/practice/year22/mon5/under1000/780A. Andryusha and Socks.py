import sys

input = sys.stdin.readline

n = int(input())
chk = [False] * (n + 1)
data = list(map(int, input().split()))

mv = -1
cnt = 0
for i in data:
    if chk[i]:
        cnt -= 1
    else:
        cnt += 1
        chk[i] = True
        mv = max(cnt, mv)

print(mv)