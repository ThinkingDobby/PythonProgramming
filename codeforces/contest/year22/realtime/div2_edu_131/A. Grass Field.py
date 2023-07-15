import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [list(map(int, input().split())) for _ in range(2)]
    cnt = data[0].count(1) + data[1].count(1)
    if cnt == 0:
        print(0)
    elif cnt == 4:
        print(2)
    else:
        print(1)