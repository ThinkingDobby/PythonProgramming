import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sv = 1
    bv = n + 1

    ans = [[0] * n, [0] * n]
    ans[0][0] = n * 2

    for j in range(n):
        for i in range(2):
            if i == j == 0:
                continue
            if (i + j) % 2 == 0:
                ans[i][j] = bv
                bv += 1
            else:
                ans[i][j] = sv
                sv += 1

    print(*ans[0])
    print(*ans[1])
