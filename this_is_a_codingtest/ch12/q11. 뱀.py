import sys

input = sys.stdin.readline


def rotate(now, dir):
    if now == 'L':
        if dir == 'L':
            return 'D'
        else:
            return 'U'
    elif now == 'R':
        if dir == 'L':
            return 'U'
        else:
            return 'D'
    elif now == 'U':
        if dir == 'L':
            return 'L'
        else:
            return 'R'
    else:
        if dir == 'L':
            return 'R'
        else:
            return 'L'


n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
rotates = []
for _ in range(l):
    x, c = input().split()
    rotates.append([int(x), c])

dirs = ['L', 'R', 'U', 'D']
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

board = []
for i in range(n):
    board.append([-1] * n)
for i in apples:
    board[i[0] - 1][i[1] - 1] = -2  # apple
board[0][0] = 0

i = 0   # rotates 순환
now = (0, 0)
vt = 1  # 방문 시점
len = 1 # 뱀 길이
cnt = rotates[0][0]
dir = 'R'
flag = True
while True:
    for j in range(cnt):
        now = (now[0] + move[dir][0], now[1] + move[dir][1])

        if not(0 <= now[0] < n) or not(0 <= now[1] < n):
            flag = False
            break

        if board[now[0]][now[1]] == -2:
            len += 1
        elif vt - board[now[0]][now[1]] <= len:
            flag = False
            break
        board[now[0]][now[1]] = vt
        vt += 1

    if not flag:
        break

    dir = rotate(dir, rotates[i][1])
    i += 1
    if i >= l:
        cnt = n
    else:
        cnt = rotates[i][0] - rotates[i - 1][0]

print(vt)

# 방문 시점을 기록하고 재방문 시 시간차를 길이와 비교하는 방법으로 풀이
# 사과 -> -2로 표현
# 주의: 방향 전환 최적화 안되어있음