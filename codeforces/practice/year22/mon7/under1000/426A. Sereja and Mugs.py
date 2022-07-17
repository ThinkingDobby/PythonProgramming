import sys

input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

print("YES" if s - (sum(data) - max(data)) >= 0 else "NO")