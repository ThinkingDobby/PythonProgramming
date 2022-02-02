n = int(input())
data = list(map(int, input().split()))
memo = {}

for i in range(n):
    if data[i] in memo:
        memo[data[i]] = (memo[data[i]][0] + 1, i)
    else:
        memo[data[i]] = (1, i)

print(sorted(memo, key=lambda x: (-memo[x][0], memo[x][1]))[0])