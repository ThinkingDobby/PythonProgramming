import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
cnt = c * 2
if a == b:
    cnt += a * 2
else:
    cnt += min(a, b) * 2 + 1
print(cnt)