import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tmp = int(math.sqrt(n))
    ans = tmp - 2 + (n + tmp - 1) // tmp
    print(ans)