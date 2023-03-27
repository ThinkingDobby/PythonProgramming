import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    n -= 1

    tmp = int(math.sqrt(n))
    if tmp * tmp > n:
        tmp -= 1

    print(tmp)