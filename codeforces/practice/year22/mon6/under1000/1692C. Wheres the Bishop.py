import sys

input = sys.stdin.readline

for _ in range(int(input())):
    input()
    data = [input() for _ in range(8)]
    cnts = [data[i].count('#') for i in range(8)]
    for i in range(1, 7):
        if cnts[i - 1] == 2 and cnts[i] == 1 and cnts[i + 1] == 2:
            for j in range(8):
                if data[i][j] == '#':
                    print(i + 1, j + 1)
                    break
