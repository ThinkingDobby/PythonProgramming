import math
import sys

input = sys.stdin.readline

n = int(input())

tmp = int(math.sqrt(n))
if tmp * tmp < n:
    print(tmp + 1)
else:
    print(tmp)