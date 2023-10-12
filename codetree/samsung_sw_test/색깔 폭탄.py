import collections
import heapq
import sys

input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(data, i, j, visited, remove=False):   # 그룹 탐색 (if remove: 제거)
    n = len(data)
    red_visited = [[0] * n for _ in range(n)]   # 빨강은 모든 그룹에서 탐색될 수 있도록

    color = data[i][j]
    base_i = i
    base_j = j

    dq = collections.deque()
    dq.append((i, j))
    visited[i][j] = True

    if remove:
        data[i][j] = -2

    cnt = 1
    red_cnt = 0

    while dq:
        i, j = dq.pop()

        for r, c in dirs:
            ni = i + r
            nj = j + c
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if data[ni][nj] == color: # 같은 색이면
                    dq.append((ni, nj))
                    cnt += 1
                    if base_i < ni:
                        base_i = ni
                        base_j = nj
                    elif base_i == ni:
                        base_j = min(base_j, nj)
                    visited[ni][nj] = True

                    if remove:  # 삭제 루틴의 경우
                        data[ni][nj] = -2    # 공백으로

                elif data[ni][nj] == 0 and not red_visited[ni][nj]:   # 빨강이면
                    dq.append((ni, nj))
                    cnt += 1
                    red_cnt += 1
                    red_visited[ni][nj] = True

                    if remove:
                        data[ni][nj] = -2

    return cnt, red_cnt, base_i, base_j, color


def remove_group(data, i, j):
    visited = [[False] * n for _ in range(n)]

    bfs(data, i, j, visited, True)


def adopt_gravity(data):
    n = len(data)

    for j in range(n):
        base = n    # 벽 또는 이전 돌의 i 좌표
        i = n - 1
        memo = []   # 폭탄만 저장
        while i >= -1:
            if data[i][j] == -1 or i == -1: # 돌을 만나거나 벽을 만난 경우
                tmp = memo + [-2] * ((base - i - 1) - len(memo))
                for k in range(base - i - 1):
                    data[base - 1 - k][j] = tmp[k]

                memo = []
                base = i
            elif data[i][j] != -2:  # 공백이 아닌 경우
                memo.append(data[i][j])

            i -= 1


def rotate(data):
    n = len(data)
    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[n - j - 1][i] = data[i][j]

    return new


n, m = map(int, input().split())    # 격자 크기, 폭탄 종류 (빨강 제외)

data = [list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]

    memo = []   # 폭탄 그룹 저장
    for i in range(n):
        for j in range(n):
            if data[i][j] not in (0, -1, -2) and not visited[i][j]:   # 빨강, 돌, 공백이 아니면
                tmp = bfs(data, i, j, visited)
                if tmp[0] != 1: # 그룹 크기 1보다 큰 경우에만
                    # 그룹의 (크기, red_cnt, base_i, base_j, 색상) 저장
                    heapq.heappush(memo, (-tmp[0], tmp[1], -tmp[2], tmp[3], tmp[4]))   # 크기, base_i(행)은 음수 취함 - 정렬 위함

    if len(memo) == 0:
        break

    cnt, red_cnt, base_i, base_j, color = heapq.heappop(memo)
    cnt = -cnt
    base_i = -base_i
    remove_group(data, base_i, base_j)
    ans += cnt * cnt

    adopt_gravity(data)

    data = rotate(data)

    adopt_gravity(data)

print(ans)