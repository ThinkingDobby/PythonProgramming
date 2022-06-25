import math
import sys

input = sys.stdin.readline

n = int(input())

for i in range(int(math.sqrt(n)), -1, -1):
    if n % i == 0:
        print(i, n // i)
        break