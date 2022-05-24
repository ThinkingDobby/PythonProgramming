import sys

input = sys.stdin.readline

n, d = map(int, input().split())
cnt = 0
data = input().rstrip()

now = 0
while True:
    flag = False
    for i in range(min(n - 1, now + d), now, -1):
        if data[i] == "1":
            flag = True
            cnt += 1
            now = i
            break

    if now == n - 1:
        break
    if not flag:
        cnt = -1
        break

print(cnt)
