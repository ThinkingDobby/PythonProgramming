# WA - 원인 파악 불가

import sys

sys.stdin = open("input.txt", "r")

dirs = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


def change_way(now):
    if now == 1: return 2
    elif now == 2: return 1
    elif now == 3: return 4
    elif now == 4: return 3


def get_count(n, memo):
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in memo[i][j]:
                cnt += k[1]

    return cnt


def move(n, memo):
    cell_loc = {}

    # 통합
    for i in range(n):
        for j in range(n):
            if memo[i][j]:
                cnt = 0
                midx = mv = mway = -1
                for cell in memo[i][j]:
                    cnt += cell[1]
                    if mv < cell[1]:
                        mv = cell[1]
                        midx = cell[0]
                        mway = cell[2]
                memo[i][j] = [[midx, cnt, mway]]
                cell_loc[midx] = [i, j]

    # 이동
    for key in cell_loc:
        i, j = cell_loc[key]
        if memo[i][j]:
            for cell in memo[i][j]:
                if cell[0] == key:
                    if 0 <= i + dirs[cell[2]][0] < n and 0 <= j + dirs[cell[2]][1] < n:
                        if i + dirs[cell[2]][0] in (0, n - 1) or j + dirs[cell[2]][1] in (0, n - 1):
                            if cell[1] // 2 > 0:
                                memo[i][j].remove(cell)
                                memo[i + dirs[cell[2]][0]][j + dirs[cell[2]][1]].append([cell[0], cell[1] // 2, change_way(cell[2])])
                        else:
                            memo[i][j].remove(cell)
                            memo[i + dirs[cell[2]][0]][j + dirs[cell[2]][1]].append([cell[0], cell[1], cell[2]])

    # for i in range(n):
    #     for j in range(n):
    #         print(memo[i][j], end=' ')
    #     print()
    # print()

def solve():
    result = ""
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(k)]  # 세로, 가로, 미생물 수, 방향

        memo = [[list() for _ in range(n)] for _ in range(n)]  # 인덱스, 미생물 수, 방향
        for i in range(k):
            memo[data[i][0]][data[i][1]].append([i, data[i][2], data[i][3]])

        for time in range(m):   # m번의 이동
            move(n, memo)

        result += f"#{t + 1} {get_count(n, memo)}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")