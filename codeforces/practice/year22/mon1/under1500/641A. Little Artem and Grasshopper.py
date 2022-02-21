n = int(input())
dir = list(input())
len = list(map(int, input().split()))

now = 0
flag = True
for i in range(n):
    if dir[now] == '>':
        now += len[now]
    else:
        now -= len[now]
    if now < 0 or now >= n:
        flag = False
        break

if flag:
    print("INFINITE")
else:
    print("FINITE")
