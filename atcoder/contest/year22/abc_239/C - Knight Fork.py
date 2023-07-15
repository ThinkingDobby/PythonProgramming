import sys

input = sys.stdin.readline

memo = [2, 10, 16, 4, 18, 20]
x1, y1, x2, y2 = map(int, input().split())
if ((x1 - x2)**2 + (y1 - y2)**2) in memo:
    print("Yes")
else:
    print("No")