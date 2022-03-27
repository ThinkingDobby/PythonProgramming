import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [list(map(int, input().split())) for _ in range(3)]
    sdata = sorted(data, key=lambda x: x[1])
    if sdata[-2][1] == sdata[-1][1] and sdata[-1][1] > sdata[0][1]:
        print(abs(sdata[-2][0] - sdata[-1][0]))
    else:
        print(0)
