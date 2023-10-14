# WA


import math
import sys

input = sys.stdin.readline

dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))


def check_way(data, i, j, ei, ej):
    r = 1 if ei > i else -1
    c = 1 if ej > j else -1

    if ei != i:
        if data[i + r][j] <= 0:
            return i + r, j

    if ej != j:
        if data[i][j + c] <= 0:
            return i, j + c

    return i, j


def get_square(person_loc, person_quit, ei, ej):
    m = len(person_loc)

    dist = math.inf
    si = sj = 0

    for p_idx in range(m):
        if not person_quit[p_idx]:
            i, j = person_loc[p_idx]
            tmp = max(abs(ei - i), abs(ej - j))
            if tmp < dist:
                dist = tmp
                si = i
                sj = j
            elif tmp == dist and si > i:
                si = i
                sj = j
            elif tmp == dist and si == i and sj > j:
                si = i
                sj = j

    return max(0, max(si, ei) - dist), max(0, max(sj, ej) - dist), dist + 1


def rotate(data, person_data, person_loc, si, sj, s_len):
    new = [[0] * s_len for _ in range(s_len)]
    tmp = [[0] * s_len for _ in range(s_len)]

    new_person = [[list() for _ in range(s_len)] for _ in range(s_len)]
    tmp_person = [[list() for _ in range(s_len)] for _ in range(s_len)]

    for i in range(s_len):
        for j in range(s_len):
            tmp[i][j] = data[si + i][sj + j]
            tmp_person[i][j] = person_data[si + i][sj + j]

    for i in range(s_len):
        for j in range(s_len):
            new[i][j] = tmp[s_len - 1 - j][i]
            new_person[i][j] = tmp_person[s_len - 1 - j][i]

    for i in range(s_len):
        for j in range(s_len):
            data[si + i][sj + j] = new[i][j]
            person_data[si + i][sj + j] = new_person[i][j]

            if data[si + i][sj + j] == -1:
                exit_loc[0] = si + i
                exit_loc[1] = sj + j
            elif data[si + i][sj + j] > 0:
                data[si + i][sj + j] -= 1

            if person_data[si + i][sj + j]:
                for p_idx in person_data[si + i][sj + j]:
                    person_loc[p_idx][0] = si + i
                    person_loc[p_idx][1] = sj + j


n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

person_loc = [[-1, -1] for _ in range(m)]   # 각 사람 위치
move_cnt = 0    # 총 이동 횟수
person_data = [[list() for _ in range(n)] for _ in range(n)]    # 각 칸의 사람
person_quit = [False] * m

for p_idx in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    person_data[i][j].append(p_idx)
    person_loc[p_idx][0] = i
    person_loc[p_idx][1] = j

exit_loc = list(map(lambda x: int(x) - 1, input().split()))  # 출구 위치
data[exit_loc[0]][exit_loc[1]] = -1

for time in range(k):
    ei = exit_loc[0]
    ej = exit_loc[1]

    for p_idx in range(m):
        if person_quit[p_idx]:  # 나갔으면 고려 x
            continue

        i, j = person_loc[p_idx]
        ni, nj = check_way(data, i, j, ei, ej)

        if not (i == ni and j == nj):
            move_cnt += 1

        person_data[i][j].remove(p_idx)
        if ni == ei and nj == ej:   # 출구면
            person_quit[p_idx] = True
        else:   # 빈칸이면
            person_loc[p_idx][0] = ni
            person_loc[p_idx][1] = nj
            person_data[ni][nj].append(p_idx)

    if all(person_quit):    # 모두 나가면 종료
        break

    si, sj, s_len = get_square(person_loc, person_quit, ei, ej)

    rotate(data, person_data, person_loc, si, sj, s_len)

print(move_cnt)
print(exit_loc[0] + 1, exit_loc[1] + 1)