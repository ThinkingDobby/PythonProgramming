# WA

import sys

sys.stdin = open("input.txt", "r")


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def progress(memo, w, h, i, j, k):
    if memo[i][j][1] > k or memo[i][j][0] == 0:
        return

    for a, b in dirs:
        if 0 <= i + a < h and 0 <= j + b < w:
            if memo[i + a][j + b][0] == 0:
                memo[i + a][j + b][0] = memo[i][j][0]
                memo[i + a][j + b][1] = sum(memo[i][j]) + 1
            elif memo[i + a][j + b][1] > sum(memo[i][j]) + 1:
                memo[i + a][j + b][0] = memo[i][j][0]
                memo[i + a][j + b][1] = sum(memo[i][j]) + 1
            elif memo[i + a][j + b][1] == sum(memo[i][j]) + 1 and memo[i + a][j + b][0] < memo[i][j][0]:
                memo[i + a][j + b][0] = memo[i][j][0]
                memo[i + a][j + b][1] = sum(memo[i][j]) + 1
            else:
                continue

            progress(memo, w, h, i + a, j + b, k)
            if i + a == k + 1 and j + b == k + 3:
                print(i, j, memo[i][j], memo[k + 2][k + 3])


def solve():
    result = ""

    for t in range(int(input())):
        n, m, k = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]
        memo = [[[0, 0] for _ in range(m + k * 2)] for _ in range(n + k * 2)]

        for i in range(n):
            for j in range(m):
                memo[i + k][j + k][0] = data[i][j]    # 생명력, 생성 시간
                memo[i + k][j + k][1] = 0

        for i in range(n):
            for j in range(m):
                progress(memo, m + k * 2, n + k * 2, i + k, j + k, k)

        cnt = 0
        for i in range(n + k * 2):
            for j in range(m + k * 2):
                print(memo[i][j][0], end=' ')
                if memo[i][j][1] <= k <= sum(memo[i][j]) + memo[i][j][0] - 1:
                    cnt += 1
            print()

        result += f"#{t + 1} {cnt}\n"


    return result


result = solve()
print(result)


with open("sample_output.txt", "r") as file:
    output = file.read()

if result.rstrip() == output.rstrip():
    print("Correct")
else:
    print("Wrong")