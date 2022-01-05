import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n, k = map(int, inp().split())

    data = []
    memo = [0 for i in range(n)]

    for _ in range(n):
        data.append(list(map(int, inp().split())))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1]) <= k:
                memo[i] += 1
                memo[j] += 1

    if max(memo) < n - 1:
        print(-1)
    else:
        print(1)