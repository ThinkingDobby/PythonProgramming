import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int, input().split())

    print(int(math.log2(r)))