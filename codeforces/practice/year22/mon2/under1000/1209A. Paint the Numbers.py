n = int(input())
data = sorted(map(int, input().split()))
memo = [True for i in range(n)]

cnt = 0
for i in range(n):
    if not memo[i]:
        continue
    cnt += 1
    for j in range(i, n):
        if data[j] % data[i] == 0:
            memo[j] = False

print(cnt)
