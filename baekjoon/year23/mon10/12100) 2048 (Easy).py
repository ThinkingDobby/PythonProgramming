# WA - 10%

import sys

input = sys.stdin.readline


def tilt(data, n, way):
    if way == 0:    # 좌
        for i in range(n):
            new = []
            memo = [data[i][j] for j in range(n) if data[i][j] != 0] + [-1]

            j = 1
            while j < len(memo):
                if memo[j - 1] == memo[j]:
                    new.append(memo[j - 1] + memo[j])
                    j += 1
                else:
                    new.append(memo[j - 1])

                j += 1
            data[i] = new + [0] * (n - len(new))
    elif way == 1:  # 우
        for i in range(n):
            new = []
            memo = [data[i][j] for j in range(n - 1, -1, -1) if data[i][j] != 0] + [-1]

            j = 1
            while j < len(memo):
                if memo[j - 1] == memo[j]:
                    new.append(memo[j - 1] + memo[j])
                    j += 1
                else:
                    new.append(memo[j - 1])

                j += 1
            data[i] = [0] * (n - len(new)) + list(reversed(new))
    elif way == 2:  # 상
        for j in range(n):
            new = []
            memo = [data[i][j] for i in range(n) if data[i][j] != 0] + [-1]

            i = 1
            while i < len(memo):
                if memo[i - 1] == memo[i]:
                    new.append(memo[i - 1] + memo[i])
                    i += 1
                else:
                    new.append(memo[i - 1])

                i += 1

            tmp = new + [0] * (n - len(new))
            for i in range(n):
                data[i][j] = tmp[i]
    elif way == 3:  # 하
        for j in range(n):
            new = []
            memo = [data[i][j] for i in range(n - 1, -1, -1) if data[i][j] != 0] + [-1]

            i = 1
            while i < len(memo):
                if memo[i - 1] == memo[i]:
                    new.append(memo[i - 1] + memo[i])
                    i += 1
                else:
                    new.append(memo[i - 1])

                i += 1

            tmp = [0] * (n - len(new)) + list(reversed(new))
            for i in range(n):
                data[i][j] = tmp[i]

        # for i in range(n):
        #     print(data[i])


def get_max(data):
    mv = -1
    for i in data:
        mv = max(mv, max(i))
    return mv


def dfs(data, n, way, lev):
    if lev > 5:
        return get_max(data)

    tilt(data, n, way)

    mv = -1
    for i in range(4):
        mv = max(mv, dfs(data[:], n, i, lev + 1))
    return mv


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

mv = -1
for i in range(4):
    mv = max(mv, dfs(data[:], n, i, 1))

print(mv)

"""
4
4 2 0 0
0 0 0 0
0 0 0 0
2 0 0 0
"""

"""
4
2 4 16 8
8 4 0 0
16 8 2 0
2 8 2 0
"""