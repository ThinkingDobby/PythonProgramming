import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    n = x - y
    print("YES" if n > 1 else "NO")