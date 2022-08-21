import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = sorted(map(int, input().split()))

    now = 0
    for i in range(1, n):
        now = now + data[i] + 1

    if now < m - data[0] and now + data[-1] < m:
        print("YES")
    else:
        print("NO")