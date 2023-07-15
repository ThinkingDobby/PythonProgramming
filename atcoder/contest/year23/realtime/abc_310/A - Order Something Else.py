import sys

input = sys.stdin.readline

n, p, q = map(int, input().split())
d = list(map(int, input().split()))

ans = min(p, min(d) + q)
print(ans)