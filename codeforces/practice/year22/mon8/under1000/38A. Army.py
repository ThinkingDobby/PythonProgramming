import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())
ans = sum(d[a - 1:b - 1])
print(ans)