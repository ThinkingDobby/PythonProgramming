import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
f = (k + 2 * m - 1) // (2 * m)
tmp = (k + 2 * m - 1) % (2 * m) + 1
s = (tmp + 1) // 2
t = 'L' if tmp % 2 == 1 else 'R'

print(f, s, t)