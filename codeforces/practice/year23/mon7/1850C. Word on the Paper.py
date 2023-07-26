import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [input().rstrip() for _ in range(8)]

    check = False
    for i in range(8):
        for j in range(8):
            if data[i][j] != '.':
                check = True
                for k in range(i, 8):
                    if data[k][j] == '.':
                        break
                    print(data[k][j], end='')
                print()
                break
        if check:
            break
