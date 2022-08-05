import sys

input = sys.stdin.readline

n = int(input())
now = 2

for i in range(n - 1):
    print(now % n if now % n != 0 else n, end=' ')
    now += (i + 2)
