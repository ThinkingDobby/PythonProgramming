import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(input().rstrip()) for _ in range(n)]

    cnt_row = [0] * n
    cnt_col = [0] * m

    for i in range(n):
        for j in range(m):
            if data[i][j] != '.':
                cnt_row[i] += 1
                cnt_col[j] += 1

    if all(map(lambda x: x % 2 == 0, cnt_row)) and all(map(lambda x: x % 2 == 0, cnt_col)):
        for i in range(n):
            cnt = 0
            for j in range(m):
                if data[i][j] == 'U':
                    cnt += 1

            cnt //= 2
            for j in range(m):
                if data[i][j] == 'U':
                    if cnt > 0:
                        data[i][j] = 'B'
                        data[i + 1][j] = 'W'
                        cnt -= 1
                    else:
                        data[i][j] = 'W'
                        data[i + 1][j] = 'B'

        for j in range(m):
            cnt = 0
            for i in range(n):
                if data[i][j] == 'L':
                    cnt += 1

            cnt //= 2
            for i in range(n):
                if data[i][j] == 'L':
                    if cnt > 0:
                        data[i][j] = 'B'
                        data[i][j + 1] = 'W'
                        cnt -= 1
                    else:
                        data[i][j] = 'W'
                        data[i][j + 1] = 'B'

        for i in range(n):
            print(''.join(data[i]))

    else:
        print(-1)
