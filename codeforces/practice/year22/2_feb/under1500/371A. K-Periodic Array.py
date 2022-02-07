n, k = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(k):
    memo = {}
    for j in range(i, n, k):
        memo[data[j]] = memo[data[j]] + 1 if data[j] in memo else 1
    cnt += sum(memo.values()) - max(memo.values())

print(cnt)