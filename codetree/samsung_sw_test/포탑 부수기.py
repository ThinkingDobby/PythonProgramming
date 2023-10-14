import collections
import heapq
import math

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))   # 우 하 좌 상


def find_turret(data, attack_timing):
    n = len(data)
    m = len(data[0])

    check_weak = []
    check_strong = []

    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                heapq.heappush(check_weak, (data[i][j], -attack_timing[i][j], -(i + j), -j, i, j)) # 4:i, 5:j
                heapq.heappush(check_strong, (-data[i][j], attack_timing[i][j], (i + j), j, i, j))

    attacker = heapq.heappop(check_weak)
    target = heapq.heappop(check_strong)

    return attacker[4], attacker[5], target[4], target[5]  # 공격자, 공격대상 좌표


def bfs(data, ai, aj, ti, tj):
    n = len(data)
    m = len(data[0])
    dists = [[math.inf] * m for _ in range(n)]

    dq = collections.deque()
    dq.append((ai, aj, 0))
    dists[ai][aj] = 0

    while dq:
        i, j, lev = dq.popleft()

        for r, c in dirs:
            ni = (i + r) % n
            nj = (j + c) % m
            if lev + 1 < dists[ni][nj] and data[ni][nj] > 0:
                # print(i, j, ni, nj)
                dq.append((ni, nj, lev + 1))
                dists[ni][nj] = lev + 1

    # for i in dists:
    #     print(i)

    return dists[ti][tj]


def dfs(data, i, j, ti, tj, visited, cnt):
    global dist, path, flag
    if cnt > dist:
        return
    if i == ti and j == tj and not flag:
        flag = True

        return [(i, j)]

    visited[i][j] = True
    for r, c in dirs:
        ni = (i + r) % n
        nj = (j + c) % m

        if not visited[ni][nj] and data[ni][nj] > 0:
            result = dfs(data, ni, nj, ti, tj, visited, cnt + 1)
            if result:
                return result + [(i, j)]
            visited[ni][nj] = False

    return


def lazer(data, ai, aj, ti, tj, path, now_attacked):
    for ni, nj in path:
        if not (ni == ai and nj == aj):
            if ni == ti and nj == tj:  # 공격 대상
                data[ni][nj] -= data[ai][aj]
            else:  # 부공격 대상
                data[ni][nj] -= (data[ai][aj]) // 2

            now_attacked[ni][nj] = True


def cannon(data, ai, aj, ti, tj, now_attacked):
    n = len(data)
    m = len(data[0])

    for r in range(-1, 2):
        for c in range(-1, 2):
            ni = (ti + r) % n
            nj = (tj + c) % m
            if not (ni == ai and nj == aj) and data[ni][nj] > 0:
                if ni == ti and nj == tj:   # 공격 대상
                    data[ni][nj] -= data[ai][aj]
                else:   # 부공격 대상
                    data[ni][nj] -= (data[ai][aj]) // 2

                now_attacked[ni][nj] = True


n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
attack_timing = [[0] * m for _ in range(n)] # 공격한 시간 저장

for time in range(1, k + 1):
    ai, aj, ti, tj = find_turret(data, attack_timing)
    if ai == ti and aj == tj:   # 포탑 하나 남은 경우
        break

    attack_timing[ai][aj] = time
    data[ai][aj] += (n + m)

    visited = [[False] * m for _ in range(n)]

    dist = bfs(data, ai, aj, ti, tj)

    now_attacked = [[False] * m for _ in range(n)]
    if dist != math.inf:
        flag = False

        path = list(reversed(dfs(data, ai, aj, ti, tj, visited, 0)))
        # print(path)
        lazer(data, ai, aj, ti, tj, path, now_attacked)
    else:   # 포탑 공격
        cannon(data, ai, aj, ti, tj, now_attacked)
    # print(ai, aj, ti, tj)
    # print(path)

    for i in range(n):
        for j in range(m):
            if not (i == ai and j == aj) and not now_attacked[i][j] and data[i][j] > 0:
                data[i][j] += 1

    # for i in data:
    #     print(i)
    # print()

mv = -1
for i in range(n):
    mv = max(mv, max(data[i]))

print(mv)