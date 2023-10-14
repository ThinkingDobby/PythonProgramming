# WA

import collections
import sys

input = sys.stdin.readline

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(data, group, si, sj, group_cnt):
    n = len(data)

    dq = collections.deque()

    dq.append((si, sj))
    group[si][sj] = group_cnt

    while dq:
        i, j = dq.popleft()

        for r, c in dirs:
            ni = i + r
            nj = j + c
            if 0 <= ni < n and 0 <= nj < n and data[ni][nj] != 0 and group[ni][nj] == -1:
                dq.append((ni, nj))
                group[ni][nj] = group_cnt


def init_group(data, group):
    group_cnt = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and group[i][j] == -1:
                bfs(data, group, i, j, group_cnt)
                group_cnt += 1


def init_head_tail(data, group, head, tail):
    n = len(data)

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                head[group[i][j]] = [i, j]
            elif data[i][j] == 3:
                tail[group[i][j]] = [i, j]


def move(data, group_num, head, tail):
    n = len(data)

    hi, hj = head[group_num]
    ti, tj = tail[group_num]

    check_connected = True

    for r, c in dirs:
        ni = hi + r
        nj = hj + c

        if 0 <= ni < n and 0 <= nj < n and data[ni][nj] == 4:
            check_connected = False
            data[ni][nj] = 1
            data[hi][hj] = 2
            head[group_num] = [ni, nj]

    for r, c in dirs:
        ni = ti + r
        nj = tj + c

        if 0 <= ni < n and 0 <= nj < n and data[ni][nj] == 2:
            data[ni][nj] = 3
            data[ti][tj] = 4
            tail[group_num] = [ni, nj]

    if check_connected: # 머리 바로 앞에 꼬리 있는 경우
        data[hi][hj] = 2
        data[ti][tj] = 1
        head[group_num] = [ti, tj]


def reverse_group(data, group_num, head, tail):
    hi, hj = head[group_num]
    ti, tj = tail[group_num]

    head[group_num] = [ti, tj]
    tail[group_num] = [hi, hj]

    data[ti][tj] = 1
    data[hi][hj] = 3


def check_order(head, group_num, ti, tj):
    hi, hj = head[group_num]
    if hi == ti and hj == tj:
        return 1

    dq = collections.deque()

    dq.append((hi, hj, 1))
    check = False

    while dq:
        i, j, cnt = dq.popleft()

        for r, c in dirs:
            ni = i + r
            nj = j + c
            if 0 <= ni < n and 0 <= nj < n:
                if ti == ni and tj == nj:
                    if data[ni][nj] == 3 and not check:
                        continue
                    else:
                        return cnt + 1
                elif data[ni][nj] == 2:
                    dq.append((ni, nj, cnt + 1))
                    check = True    # 바로 이어진 3으로 가지 않도록 (2를 한번은 거치도록)


def check_ball_hit(data, group, rnd):
    n = len(data)
    typ = (rnd // n) % 4

    if typ == 0 or typ == 1:
        k = rnd % n
    elif typ == 2 or typ == 3:
        k = n - 1 - rnd % n

    group_num = -1
    ni = nj = -1

    if typ == 0:
        for j in range(n):
            if data[k][j] != 0 and data[k][j] != 4:
                group_num = group[k][j]
                ni, nj = k, j
                break

    elif typ == 1:
        for i in range(n - 1, -1, -1):
            if data[i][k] != 0 and data[i][k] != 4:
                group_num = group[i][k]
                ni, nj = i, k
                break

    elif typ == 2:
        for j in range(n - 1, -1, -1):
            if data[k][j] != 0 and data[k][j] != 4:
                group_num = group[k][j]
                ni, nj = k, j
                break

    elif typ == 3:
        for i in range(n):
            if data[i][k] != 0 and data[i][k] != 4:
                group_num = group[i][k]
                ni, nj = i, k
                break

    if group_num != -1: # 받은 사람 있으면
        tmp = check_order(head, group_num, ni, nj)
        reverse_group(data, group_num, head, tail)

        return tmp**2

    return 0


n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
group = [[-1] * n for _ in range(n)]

head = [[-1, -1] for _ in range(m)]
tail = [[-1, -1] for _ in range(m)]

init_group(data, group)
init_head_tail(data, group, head, tail)

score = 0
for rnd in range(k):
    for group_num in range(m):
        move(data, group_num, head, tail)

    score += check_ball_hit(data, group, rnd)

print(score)