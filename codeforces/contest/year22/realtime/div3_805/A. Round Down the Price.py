import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    tmp = int(math.log10(m))
    print(m - 10**tmp)