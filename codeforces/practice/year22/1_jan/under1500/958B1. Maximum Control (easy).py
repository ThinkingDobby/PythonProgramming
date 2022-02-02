memo = [0] * 1001

for _ in range(int(input()) - 1):
    u, v = map(int, input().split())
    memo[u] += 1
    memo[v] += 1

print(len([i for i in memo if i == 1]))