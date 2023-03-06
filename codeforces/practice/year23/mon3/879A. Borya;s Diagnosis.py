import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

mv = data[0][0]
for i in range(1, n):
    if data[i][0] < mv:
        tmp = (mv - data[i][0] + data[i][1]) // data[i][1]
        mv = data[i][0] + tmp * data[i][1]
    elif data[i][0] == mv:
        mv = data[i][0] + data[i][1]
    else:
        mv = data[i][0]

print(mv)