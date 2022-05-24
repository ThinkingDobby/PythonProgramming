import math
import sys

input = sys.stdin.readline
mod = 998_244_353

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1:
        print(0)
    else:
        tmp = n // 2
        ans = 1
        while tmp:
            ans = (ans * tmp) % mod
            tmp -= 1
        print((ans * ans) % mod)