# TLE

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    print(min(2 ** k, n + 1))