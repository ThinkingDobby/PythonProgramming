import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    memo = dict()
    for i in range(n):
        if data[i] in memo:
            mv = sorted([memo[data[i]][1], memo[data[i]][2], i - memo[data[i]][0]])
            memo[data[i]][0] = i
            memo[data[i]][1] = mv[2]
            memo[data[i]][2] = mv[1]
        else:
            memo[data[i]] = [i, i - (-1), 0]

    for i in memo:
        mv = sorted([memo[i][1], memo[i][2], n - memo[i][0]])
        memo[i][0] = n
        memo[i][1] = mv[2]
        memo[i][2] = mv[1]

    tmp = min([max([(i[1] + 1) // 2, i[2]]) for i in memo.values()])
    print(tmp - 1)
