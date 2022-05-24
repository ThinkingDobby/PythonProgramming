import sys

input = sys.stdin.readline

n, k = map(int, input().split())

tmp = (n // 2) // (k + 1)
print(tmp, tmp * k, n - (tmp + tmp * k))