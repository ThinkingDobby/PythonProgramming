import sys

input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(3)]

memo = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def chk(x, y):
    return 0 <= x < 3 and 0 <= y < 3


tmp = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(3):
    for j in range(3):
        for now in tmp:
            if chk(i + now[0], j + now[1]):
                memo[i + now[0]][j + now[1]] += data[i][j]

for i in range(3):
    for j in range(3):
        print(0 if memo[i][j] % 2 == 0 else 1, end='')
    print()
