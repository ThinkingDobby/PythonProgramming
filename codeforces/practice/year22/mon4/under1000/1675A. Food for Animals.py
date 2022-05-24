import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    if c - (max(0, x - a) + max(0, y - b)) < 0:
        print("NO")
    else:
        print("YES")