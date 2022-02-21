memo = {}
for i in range(int(input())):
    h, m = map(int, input().split())
    tmp = h * 60 + m
    memo[tmp] = memo[tmp] + 1 if tmp in memo else 1

print(max(memo.values()))