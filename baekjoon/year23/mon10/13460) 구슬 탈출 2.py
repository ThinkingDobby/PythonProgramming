import math
import sys

input = sys.stdin.readline

dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 0: 상, 1: 좌, 2: 하, 3: 우


def move(data, way, ni, nj, oi, oj):  # ni, nj: 현재 구슬, oi, oj: 상대 구슬
    new_ni = ni
    new_nj = nj

    while not (data[new_ni + dirs[way][0]][new_nj + dirs[way][1]] == '#'
               or (new_ni + dirs[way][0] == oi and new_nj + dirs[way][1] == oj)):
        new_ni += dirs[way][0]
        new_nj += dirs[way][1]

        if data[new_ni][new_nj] == 'O':
            return True, -1, -1  # 다음 구슬의 이동에 영향을 주지 않도록

    return False, new_ni, new_nj


def check_and_move(data, way, cnt, ri, rj, bi, bj):
    if cnt > 10:
        return math.inf

    if way == 0:  # 상
        if rj == bj and ri < bi:  # j좌표 같으면 더 위에 있는 구슬부터 이동
            chk_r, new_ri, new_rj = move(data, way, ri, rj, bi, bj)
            chk_b, new_bi, new_bj = move(data, way, bi, bj, new_ri, new_rj)
        else:
            chk_b, new_bi, new_bj = move(data, way, bi, bj, ri, rj)
            chk_r, new_ri, new_rj = move(data, way, ri, rj, new_bi, new_bj)
    elif way == 1:  # 좌
        if ri == bi and rj < bj:  # 왼쪽에 있는 구슬부터 이동
            chk_r, new_ri, new_rj = move(data, way, ri, rj, bi, bj)
            chk_b, new_bi, new_bj = move(data, way, bi, bj, new_ri, new_rj)
        else:
            chk_b, new_bi, new_bj = move(data, way, bi, bj, ri, rj)
            chk_r, new_ri, new_rj = move(data, way, ri, rj, new_bi, new_bj)
    elif way == 2:  # 하
        if rj == bj and ri > bi:  # 아래에 있는 구슬부터 이동
            chk_r, new_ri, new_rj = move(data, way, ri, rj, bi, bj)
            chk_b, new_bi, new_bj = move(data, way, bi, bj, new_ri, new_rj)
        else:
            chk_b, new_bi, new_bj = move(data, way, bi, bj, ri, rj)
            chk_r, new_ri, new_rj = move(data, way, ri, rj, new_bi, new_bj)
    else:   # 우
        if ri == bi and rj > bj:  # 오른쪽에 있는 구슬부터 이동
            chk_r, new_ri, new_rj = move(data, way, ri, rj, bi, bj)
            chk_b, new_bi, new_bj = move(data, way, bi, bj, new_ri, new_rj)
        else:
            chk_b, new_bi, new_bj = move(data, way, bi, bj, ri, rj)
            chk_r, new_ri, new_rj = move(data, way, ri, rj, new_bi, new_bj)

    # print(ri, rj, bi, bj, way, chk_r, chk_b, cnt)
    if chk_b:
        return math.inf
    elif chk_r:
        return cnt
    else:
        tmp = math.inf
        for new_way in range(4):
            if new_way != way:
                tmp = min(tmp, check_and_move(data, new_way, cnt + 1, new_ri, new_rj, new_bi, new_bj))
        return tmp


n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

R = [-1, -1]
B = [-1, -1]

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            R[0] = i
            R[1] = j
        elif data[i][j] == 'B':
            B[0] = i
            B[1] = j

ans = math.inf
for way in range(4):
    ans = min(ans, check_and_move(data, way, 1, R[0], R[1], B[0], B[1]))
    # print()

print(-1 if ans == math.inf else ans)
