import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = True
    mv = math.inf

    for i in range(n - 1, -1, -1):
        if data[i] > mv:
            if data[i] >= 10 and data[i] // 10 <= data[i] % 10 and data[i] % 10 <= mv:
                mv = data[i] // 10
            else:
                ans = False
                break
        else:
            mv = min(mv, data[i])

    print("YES" if ans else "NO")