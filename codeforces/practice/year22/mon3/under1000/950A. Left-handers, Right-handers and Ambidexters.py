import sys

input = sys.stdin.readline

l, r, a = map(int, input().split())

tmp = a - abs(l - r)
ans = tmp // 2 + max(l, r) if tmp >= 0 else min(l, r) + a

print(ans * 2)