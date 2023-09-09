import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

s = 0
x, y = map(int, input().split())

for _ in range(n - 1):
    a, b = map(int, input().split())

    s += math.sqrt((x - a)**2 + (y - b)**2)

    x = a
    y = b

print(s * 0.02 * k)