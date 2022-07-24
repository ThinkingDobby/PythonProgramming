import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    memo = dict()   # 0:even, 1:odd
    ans = [0 for i in range(n + 1)]

    data = list(map(int, input().split()))
    for i in range(n):
        if data[i] not in memo:
            memo[data[i]] = i % 2
            ans[data[i]] += 1
        else:
            if memo[data[i]] != i % 2:
                memo[data[i]] = i % 2
                ans[data[i]] += 1

    print(*ans[1:])
