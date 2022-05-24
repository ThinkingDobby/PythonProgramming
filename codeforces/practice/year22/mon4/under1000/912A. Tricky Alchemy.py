import sys

input = sys.stdin.readline

a, b = map(int, input().split())
x, y, z = map(int, input().split())

print(max(0, x * 2 + y - a) + max(0, y + 3 * z - b))