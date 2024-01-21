import sys

input = sys.stdin.readline

for i in range(int(input())):
    data = sorted([list(map(int, input().split())) for _ in range(4)])

    ans = abs(data[1][0] - data[2][0]) * abs(data[0][1] - data[1][1])
    print(ans)