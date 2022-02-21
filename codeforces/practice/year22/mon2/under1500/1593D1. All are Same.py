import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    mv = min(data)

    tmp = [data[i] - mv for i in range(n) if data[i] != mv]

    if tmp:
        gcd = tmp[0]
        for i in range(1, len(tmp)):
            gcd = math.gcd(tmp[i], gcd)

        print(gcd)
    else:
        print(-1)