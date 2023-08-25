import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
data = sorted(map(int, input().split()))

if k == m:
    print(data[-1] * k)
else:
    ans = (k * data[-1] + data[-2]) * m // (k + 1) + m % (k + 1) * data[-1]
    print(ans)
