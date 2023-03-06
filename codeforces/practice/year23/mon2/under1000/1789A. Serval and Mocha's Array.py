import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = False
    for i in range(n - 1):
        for j in range(i + 1, n):
            if math.gcd(data[i], data[j]) <= 2:
                ans = True
                break

    print("YES" if ans else "NO")