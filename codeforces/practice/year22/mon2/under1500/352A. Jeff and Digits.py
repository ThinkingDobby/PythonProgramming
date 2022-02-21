n = int(input())
data = list(map(int, input().split()))

cnt5 = data.count(5)
cnt0 = data.count(0)

cnt = 0
for i in range(1, cnt5 + 1):
    if (i * 5) % 9 == 0:
        cnt = i

if cnt0 == 0:
    print(-1)
else:
    ans = int('5' * cnt + '0' * cnt0)
    print(ans)