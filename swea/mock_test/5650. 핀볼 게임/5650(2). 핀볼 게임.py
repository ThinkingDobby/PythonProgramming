import collections
import sys

sys.stdin = open("input.txt", "r")

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]   # 방향, 진행 방향


def crash(data, n, i, j, wi, wj):
    if not (0 <= i < n and 0 <= j < n) or data[i][j] == 5:
        return [-wi, -wj]
    if data[i][j] == 1:
        if [wi, wj] == [0, 1]: return [0, -1]
        elif [wi, wj] == [0, -1]: return [-1, 0]
        elif [wi, wj] == [1, 0]: return [0, 1]
        elif [wi, wj] == [-1, 0]: return [1, 0]
    elif data[i][j] == 2:
        if [wi, wj] == [0, 1]: return [0, -1]
        elif [wi, wj] == [0, -1]: return [1, 0]
        elif [wi, wj] == [1, 0]: return [-1, 0]
        elif [wi, wj] == [-1, 0]: return [0, 1]
    elif data[i][j] == 3:
        if [wi, wj] == [0, 1]: return [1, 0]
        elif [wi, wj] == [0, -1]: return [0, 1]
        elif [wi, wj] == [1, 0]: return [-1, 0]
        elif [wi, wj] == [-1, 0]: return [0, -1]
    elif data[i][j] == 4:
        if [wi, wj] == [0, 1]: return [-1, 0]
        elif [wi, wj] == [0, -1]: return [0, 1]
        elif [wi, wj] == [1, 0]: return [0, -1]
        elif [wi, wj] == [-1, 0]: return [1, 0]


def find_w_hole(w_holes, type, i, j):
    pairs = w_holes[type]
    if i == pairs[0][0] and j == pairs[0][1]:
        return pairs[1]
    else:
        return pairs[0]


def search(data, n, si, sj, _i, _j, _wi, _wj, w_holes):
    i = _i
    j = _j

    wi = _wi
    wj = _wj

    cnt = 0
    while not (si == i and sj == j):
        # print(si, sj, i, j, wi, wj, cnt)
        if 0 <= i < n and 0 <= j < n:
            if data[i][j] != 0:
                if 6 <= data[i][j] <= 10:   # 웜홀 대응
                    ni, nj = find_w_hole(w_holes, data[i][j], i, j) # 새로운 좌표 탐색
                    i = ni + wi
                    j = nj + wj
                elif data[i][j] == -1:  # 블랙홀 대응
                    break
                else:   # 블록 충돌
                    wi, wj = crash(data, n, i, j, wi, wj) # 방향 전환
                    i += wi
                    j += wj
                    cnt += 1
            else:   # 단순 진행
                i += wi
                j += wj
        else:   # 벽 대응
            wi, wj = crash(data, n, i, j, wi, wj)  # 방향 전환
            i += wi
            j += wj
            cnt += 1

    return cnt


def solve():
    result = ""

    for t in range(int(input())):
        n = int(input())
        data = [list(map(int, input().split())) for _ in range(n)]

        w_holes = collections.defaultdict(list) # 웜홀 종류: 웜홀 위치
        for i in range(n):
            for j in range(n):
                if 6 <= data[i][j] <= 10:
                    w_holes[data[i][j]].append([i, j])

        ans = -1
        for i in range(n):
            for j in range(n):
                if data[i][j] == 0: # 블록, 웜홀, 블랙홀 없는 곳에서 시작
                    for way in dirs:    # 각 방향으로
                        cnt = search(data, n, i, j, i + way[0], j + way[1], way[0], way[1], w_holes)   # wi, wj: 방향
                        ans = max(ans, cnt)

        result += f"#{t + 1} {ans}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")