import sys

input = sys.stdin.readline


def chk(x):
    return 1 if x == '1' else -1


def rotate_chk(a, b):
    if memo[a][b]:
        return 0
    cnt = 0
    x, y = a, b

    for i in range(4):
        memo[x][y] = True
        cnt += chk(data[x][y])
        tmp = x
        x = y
        y = n - 1 - tmp

    return (4 - abs(cnt)) // 2


for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip() for _ in range(n)]
    memo = [[False] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += rotate_chk(i, j)

    print(cnt)
