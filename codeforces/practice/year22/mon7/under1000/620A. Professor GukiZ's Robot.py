import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

f = abs(x1 - x2)
s = abs(y1 - y2)

print(max(f, s))