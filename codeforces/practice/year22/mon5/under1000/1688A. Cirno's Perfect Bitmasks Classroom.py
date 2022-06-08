# WA

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x = bin(int(input()))[2:]
    if x == '1':
        print(3)
    else:
        print(int(x[:-1] + '1' if x[-1] == '0' else '0', 2))

