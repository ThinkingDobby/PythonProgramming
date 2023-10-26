import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

ans = sorted(data, reverse=True)[:k][-1]
print(ans)