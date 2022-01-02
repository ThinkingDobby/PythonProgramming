n, m = map(int, input().split())
x, y, d = map(int, input().split())

data = [list(map(int, input().split())) for i in range(n)]
data[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d < 0:
        d += 4


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if data[nx][ny] == 0:
        data[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = x - dy[d]
        if data[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

print(count)
