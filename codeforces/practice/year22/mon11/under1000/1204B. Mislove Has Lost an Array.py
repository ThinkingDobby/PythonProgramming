import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())

max_v = 2**r - 1 + (n - r) * 2**(r - 1)
min_v = 2**l - 1 + (n - l)

print(min_v, max_v)
