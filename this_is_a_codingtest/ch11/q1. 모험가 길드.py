n = int(input())
data = sorted(map(int, input().split()))

cnt = 0
ans = 0
for i in range(n):
    cnt += 1
    if cnt == data[i]:
        cnt = 0
        ans += 1

print(ans)


""""
5
2 3 1 2 2
"""