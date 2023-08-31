import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if k // n < 3:
    print(n - k % n)
else:
    print(0)