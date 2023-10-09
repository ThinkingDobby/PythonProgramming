# RTE
# 스택 메모리 제한 초과
# SWEA는 스택 메모리 1MB로 제한
# 이 문제의 경우 시작점과 4방향만 따져도 100*100*4 -> 내부에서의 재귀 호출 고려하면 1MB는 가볍게 넘음
# 공간복잡도 계산이 가능하다면 하면 좋지만, 대부분의 경우 어려움
# => 가능하면 재귀 대신 반복문 사용할 것
# 특히 이런 문제는 한 번 진입 후, 특정 방향으로만 진행하므로 DFS를 사용할 이유가 없음
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


def dfs(data, n, si, sj, i, j, wi, wj, cnt, w_holes):
    # print(si, sj, i, j, wi, wj, cnt)
    if si == i and sj == j:    # 시작점으로 귀한한 경우
        return cnt

    if 0 <= i < n and 0 <= j < n:
        if data[i][j] != 0:
            if 6 <= data[i][j] <= 10:   # 웜홀 대응
                ni, nj = find_w_hole(w_holes, data[i][j], i, j) # 새로운 좌표 탐색
                return dfs(data, n, si, sj, ni + wi, nj + wj, wi, wj, cnt, w_holes)
            elif data[i][j] == -1:  # 블랙홀 대응
                return cnt
            else:   # 블록 충돌
                wi, wj = crash(data, n, i, j, wi, wj) # 방향 전환
                return dfs(data, n, si, sj, i + wi, j + wj, wi, wj, cnt + 1, w_holes)
        else:   # 단순 진행
            return dfs(data, n, si, sj, i + wi, j + wj, wi, wj, cnt, w_holes)
    else:   # 벽 대응
        wi, wj = crash(data, n, i, j, wi, wj)  # 방향 전환
        return dfs(data, n, si, sj, i + wi, j + wj, wi, wj, cnt + 1, w_holes)


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
                        cnt = dfs(data, n, i, j, i + way[0], j + way[1], way[0], way[1], 0, w_holes)   # wi, wj: 방향
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