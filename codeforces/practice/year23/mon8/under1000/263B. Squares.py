import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = sorted(map(int, input().split()), reverse=True)

if k > n:
    print(-1)
else:
    print(data[k - 1], data[k - 1])