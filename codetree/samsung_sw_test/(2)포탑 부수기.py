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


def bfs(data, ai, aj, ti, tj, back_x, back_y):
    n = len(data)
    m = len(data[0])
    dists = [[math.inf] * m for _ in range(n)]

    dq = collections.deque()
    dq.append((ai, aj, 0))
    dists[ai][aj] = 0

    while dq:
        i, j, lev = dq.popleft()

        if i == ti and j == tj:
            break

        for r, c in dirs:
            ni = (i + r) % n
            nj = (j + c) % m
            if dists[ni][nj] == math.inf and data[ni][nj] > 0:
                dq.append((ni, nj, lev + 1))
                dists[ni][nj] = lev + 1

                back_x[ni][nj] = i
                back_y[ni][nj] = j

    return dists[ti][tj]


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

    back_x = [[-1] * m for _ in range(n)]
    back_y = [[-1] * m for _ in range(n)]
    dist = bfs(data, ai, aj, ti, tj, back_x, back_y)

    now_attacked = [[False] * m for _ in range(n)]
    if dist != math.inf:
        flag = False

        ni = ti
        nj = tj

        path = [(ni, nj)]
        while not (ni == ai and nj == aj):
            # print(ni, nj, back_x[ni][nj], back_y[ni][nj])
            tmp_i = back_x[ni][nj]
            tmp_j = back_y[ni][nj]
            path.append((tmp_i, tmp_j))
            ni = tmp_i
            nj = tmp_j

        path.reverse()
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