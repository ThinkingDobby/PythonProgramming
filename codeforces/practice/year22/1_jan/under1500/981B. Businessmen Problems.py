memo = {}

n = int(input())
for _ in range(n):
    a, x = map(int, input().split())
    memo[a] = x

m = int(input())
for _ in range(m):
    b, x = map(int, input().split())
    if b in memo:
        memo[b] = max(memo[b], x)
    else:
        memo[b] = x

print(sum(memo.values()))