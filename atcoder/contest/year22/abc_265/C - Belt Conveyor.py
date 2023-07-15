import sys

input = sys.stdin.readline

h, w = map(int, input().split())
data = [list(input().rstrip()) for _ in range(h)]

moves = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}


def check_dir(dir, i, j):
    return [i + moves[dir][0], j + moves[dir][1]]


f = moves[data[0][0]]
if 0 <= 0 + f[0] <= h - 1 and 0 <= 0 + f[1] <= w - 1:
    i, j = check_dir(data[0][0], 0, 0)
    while True:
        if data[i][j] == '0':
            print(-1)
            break
        f = moves[data[i][j]]
        if 0 <= i + f[0] <= h - 1 and 0 <= j + f[1] <= w - 1:
            x = i
            y = j
            i, j = check_dir(data[i][j], i, j)
            data[x][y] = '0'
        else:
            print(i + 1, j + 1)
            break
else:
    print(1, 1)
