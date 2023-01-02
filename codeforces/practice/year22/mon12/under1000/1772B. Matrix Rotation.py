import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [list(map(int, input().split())) for _ in range(2)]
    seq = [[0, 0], [0, 1], [1, 1], [1, 0]]

    ans = False
    for i in range(4):
        memo = [[0, 0], [0, 0]]
        for j in range(4):
            x = seq[(j + i) % 4][0]
            y = seq[(j + i) % 4][1]
            memo[seq[j][0]][seq[j][1]] = data[x][y]
        if memo[0][0] < memo[0][1] and memo[0][0] < memo[1][0] and memo[0][1] < memo[1][1] and memo[1][0] < memo[1][1]:
            ans = True
            break

    print("YES" if ans else "NO")


