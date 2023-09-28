import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    check = [i for i in range(1, n) if data[i][0] >= data[0][0] and data[i][1] >= data[0][1]]
    if not check:
        print(data[0][0])
    else:
        print(-1)
