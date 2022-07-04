import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]

xys = []
mv = -1
for i in range(n):
    for j in range(n):
        if data[i][j] > mv:
            mv = data[i][j]
            xys = [(i, j)]
        elif data[i][j] == mv:
            xys.append((i, j))

memo = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for x, y in xys:
    for d in directions:
        a = x
        b = y
        cnt = n - 1
        tmp = str(data[a][b])
        while cnt:
            a += d[0]
            b += d[1]
            if a >= n:
                a = 0
            if b >= n:
                b = 0
            if a < 0:
                a = n - 1
            if b < 0:
                b = n - 1
            tmp += str(data[a][b])
            cnt -= 1
        memo.append(tmp)

print(max(memo))