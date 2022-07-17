import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = [[data[i], i] for i in range(n) if data[i] < i]
    stmp = sorted(tmp, key=lambda x: (x[1], x[0]))

    cnt = 0
    for i in range(1, len(tmp)):
        if stmp[i - 1][0] < stmp[i][0]:
            cnt += 1

    print(math.comb(cnt, 2))