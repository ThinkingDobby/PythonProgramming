# WA -- 98
import collections
import heapq
import math
import sys

input = sys.stdin.readline

dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))   # 상 좌 우 하


def get_close_basecamp(data, store, basecamps, visited, t):
    n = len(data)
    now_visited = [[math.inf] * n for _ in range(n)]

    dq = collections.deque()

    si = store[0]
    sj = store[1]
    dq.append((si, sj, 0))
    now_visited[si][sj] = 0

    while dq:
        i, j, now_lev = dq.popleft()

        for r, c in dirs:
            ni = i + r
            nj = j + c
            if 0 <= ni < n and 0 <= nj < n and now_visited[ni][nj] == math.inf and visited[ni][nj] >= t + now_lev + 1:
                dq.append((ni, nj, now_lev + 1))
                now_visited[ni][nj] = now_lev + 1

    memo = []
    for i, j in basecamps:
        heapq.heappush(memo, (now_visited[i][j], i, j)) # 거리, 행, 열 작은 순

    lev, bi, bj = heapq.heappop(memo)

    print("now visited")
    for i in now_visited:
        print(i)

    return bi, bj, lev


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
stores = [] # 각 사람이 가고자하는 편의점

basecamps = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            basecamps.append((i, j))

for _ in range(m):
    stores.append(tuple(map(lambda x: int(x) - 1, input().split())))

visited = [[math.inf] * n for _ in range(n)]    # 처음에는 모든 곳으로 다 갈 수 있도록
for i in range(m):  # i: 사람 번호(시간)
    bi, bj, dist = get_close_basecamp(data, stores[i], basecamps, visited, i)

    visited[bi][bj] = i
    visited[stores[i][0]][stores[i][1]] = i + dist  # 진입 시간 + 거리
    print(bi, bj, dist)

    print("visited")
    for i in visited:
        print(i)
    print()

mv = -1
for i in range(n):
    for j in range(n):
        if visited[i][j] != math.inf:
            mv = max(mv, visited[i][j])

print(mv + 1)

