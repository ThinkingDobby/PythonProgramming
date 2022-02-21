n, m = map(int, input().split())
a, b, d = map(int, input().split())

data = [list(map(int, input().split())) for i in range(n)]
data[a][b] = 1

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 1
while True:
    flag = False
    for i in range(1, 5):
        now_d = d - i
        if now_d < 0:
            now_d += 4
        if 0 <= a + move[now_d][0] < n and 0 <= b + move[now_d][1] < m:
            if data[a + move[now_d][0]][b + move[now_d][1]] == 0:
                data[a + move[now_d][0]][b + move[now_d][1]] = 1
                a += move[now_d][0]
                b += move[now_d][1]
                d = now_d
                cnt += 1
                break
        if i == 4:
            flag = True
    if flag:
        if 0 <= a - move[d][0] < n and 0 <= b - move[d][1] < m:
            if data[a - move[d][0]][b - move[d][1]] == 0:
                a -= move[d][0]
                b -= move[d][1]
                data[a - move[d][0]][b - move[d][1]] = 1
                cnt += 1
            else:
                break
        else:
            break
print(cnt)
