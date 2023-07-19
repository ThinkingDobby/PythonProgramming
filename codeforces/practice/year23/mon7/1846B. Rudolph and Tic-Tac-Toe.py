import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [input().rstrip() for _ in range(3)]

    ans = ''

    for i in range(3):
        if len(set(data[i])) == 1:
            if data[i][0] != '.':
                ans = data[i][0]

    for j in range(3):
        if len(set([data[i][j] for i in range(3)])) == 1:
            if data[0][j] != '.':
                ans = data[0][j]

    if data[0][0] == data[1][1] == data[2][2]:
        if data[0][0] != '.':
            ans = data[0][0]

    if data[0][2] == data[1][1] == data[2][0]:
        if data[0][2] != '.':
            ans = data[0][2]

    print("DRAW" if ans == '' else ans)
