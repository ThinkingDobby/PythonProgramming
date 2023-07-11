import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    if int(math.log2(n)) + 1 > k:
        print(2**k)
    else:
        print(n + 1)