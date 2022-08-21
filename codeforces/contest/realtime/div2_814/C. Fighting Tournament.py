import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    data = list(map(int, input().split()))
    max_v = max(data)

    memo = [[-1, 0] for _ in range(n + 1)]

    midx = 0
    mv = data[midx]
    if mv == max_v:
        memo[mv] = [0, -1]
    else:
        for i in range(1, n):
            if data[i] > mv:
                memo[mv] = [midx, i - 1]
                midx = i - 1
                mv = data[i]
                if data[i] == max_v:
                    memo[mv] = [midx, -1]
                    break

    for _ in range(q):
        i, k = map(int, input().split())
        i = data[i - 1]

        if memo[i][0] == -1:
            print(0)
        else:
            if memo[i][0] < k:
                if memo[i][1] == -1:
                    print(k - memo[i][0])
                else:
                    print(min(k, memo[i][1]) - memo[i][0])
            else:
                print(0)