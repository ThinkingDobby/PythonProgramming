n = int(input())
data = list(map(int, input().split()))
memo = {}

for i in range(n):
    memo[data[i]] = i

print(sorted(memo, key=lambda x: memo[x])[0])