# wa

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    visited = [False] * n
    data = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        # 중첩된 원 고려해야

# 1
# 0 0 2 2
# 2
# 0 0 1
# 0 0 3

        xd = (x1 - data[i][0])
        yd = (y1 - data[i][1])
        if xd * xd + yd * yd < data[i][2] * data[i][2]:
            visited[i] = True

        xd = (x2 - data[i][0])
        yd = (y2 - data[i][1])
        if xd * xd + yd * yd < data[i][2] * data[i][2]:
            visited[i] = True

    print(len([i for i in visited if i]))

