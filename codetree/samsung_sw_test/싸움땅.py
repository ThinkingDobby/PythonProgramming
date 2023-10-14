import heapq
import sys

input = sys.stdin.readline

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상, 우, 하, 좌


def print_list(data):
    for i in data:
        print(*i)
    print()


def drop_gun(players, idx, gun_data, ni, nj):
    heapq.heappush(gun_data[ni][nj], -players[idx][4])
    players[idx][4] = 0


def get_gun(players, idx, gun_data, ni, nj):
    heapq.heappush(gun_data[ni][nj], -players[idx][4])
    players[idx][4] = -heapq.heappop(gun_data[ni][nj])  # 총 정보만 갱신


def rotate(player_data, way, i, j):
    n = len(player_data)

    for k in range(4):
        nway = (way + k) % 4

        ni = i + dirs[nway][0]
        nj = j + dirs[nway][1]

        if not (0 <= ni < n and 0 <= nj < n):
            continue
        elif player_data[ni][nj] != -1:
            continue

        return nway, ni, nj


def move(player_data, gun_data, players, score, idx):
    n = len(player_data)
    i, j, way, stat, gun_stat = players[idx]

    ni = i + dirs[way][0]
    nj = j + dirs[way][1]

    if not (0 <= ni < n and 0 <= nj < n):
        way = (way + 2) % 4
        ni = i + dirs[way][0]
        nj = j + dirs[way][1]
        players[idx][2] = way   # 방향 갱신

    player_data[i][j] = -1  # 기존 위치에서는 제거

    if player_data[ni][nj] != -1:  # 사람 있으면
        pidx = player_data[ni][nj]
        pi, pj, pway, pstat, pgun_stat = players[pidx]

        gap = stat + gun_stat - (pstat + pgun_stat)
        if gap > 0:
            win_idx = idx
            lose_idx = pidx
        elif gap < 0:
            win_idx = pidx
            lose_idx = idx
        else:
            win_idx = idx if stat > pstat else pidx
            lose_idx = pidx if stat > pstat else idx
        score[win_idx] += abs(gap)

        drop_gun(players, lose_idx, gun_data, ni, nj)
        get_gun(players, win_idx, gun_data, ni, nj)

        # 좌표 갱신
        player_data[ni][nj] = win_idx
        players[win_idx][0] = ni
        players[win_idx][1] = nj

        lway, li, lj = rotate(player_data, players[lose_idx][2], ni, nj)  # 패자 회전 확인
        player_data[li][lj] = lose_idx
        players[lose_idx][0] = li
        players[lose_idx][1] = lj
        players[lose_idx][2] = lway

        get_gun(players, lose_idx, gun_data, li, lj)

    else:  # 사람 없으면
        get_gun(players, idx, gun_data, ni, nj)

        # 좌표 갱신
        player_data[ni][nj] = idx
        players[idx][0] = ni
        players[idx][1] = nj


n, m, k = map(int, input().split())

gun_data = [list(map(lambda x: [-int(x)], input().split())) for _ in range(n)]  # 각 칸에 있는 총 (최대 힙 - 음수롲 저장)
player_data = [[-1] * n for _ in range(n)]  # 각 칸에 있는 사람
players = []  # 사용자 정보
score = [0] * m

for i in range(m):
    x, y, d, s = map(int, input().split())
    player_data[x - 1][y - 1] = i
    players.append([x - 1, y - 1, d, s, 0])  # i, j, way, stat, gun_stat

for _ in range(k):
    for idx in range(m):
        move(player_data, gun_data, players, score, idx)

print(*score)