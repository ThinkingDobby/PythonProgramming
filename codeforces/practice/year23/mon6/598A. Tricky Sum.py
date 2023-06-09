import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = n * (n + 1) // 2

    tmp = int(math.log2(n)) + 1
    print(s - 2 * (2**tmp - 1))