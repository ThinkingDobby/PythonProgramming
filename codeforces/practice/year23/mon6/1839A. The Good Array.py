import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = math.ceil((n - 1) / k) + 1
    print(ans)