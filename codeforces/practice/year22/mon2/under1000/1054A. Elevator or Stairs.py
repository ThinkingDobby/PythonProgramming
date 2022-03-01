import sys

input = sys.stdin.readline

x, y, z, t1, t2, t3 = map(int, input().split())

tmp = abs(x - y)
f = t1 * tmp
s = abs(z - x) * t2 + t3 * 3 + tmp * t2

print("YES" if f >= s else "NO")