import sys

input = sys.stdin.readline

t, s, x = map(int, input().split())

print("YES" if x >= t and x != t + 1 and ((x - t) % s == 0 or (x - t - 1) % s == 0) else "NO")
