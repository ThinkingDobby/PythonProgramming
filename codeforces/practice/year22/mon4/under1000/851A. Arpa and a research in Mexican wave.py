import sys

input = sys.stdin.readline

n, k, t = map(int, input().split())
if t in range(0, k + 1):
    print(t)
elif t in range(k + 1, n + 1):
    print(k)
else:
    print(k - (t - n))