n = int(input())
data = sorted(map(int, input().split()))

now = 0
cnt = 0
flag = True
for i in range(1, n + 1):
    while data[now] < i:
        now += 1
        if now == n:
            flag = False
            break
    if not flag:
        break
    cnt += 1
    now += 1
    if now == n:
        flag = False
        break

print(cnt)