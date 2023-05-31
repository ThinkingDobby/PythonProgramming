import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = sorted(map(int, input().split()))
    data = sorted(map(int, input().split()))

    f = (data[-1] - data[0]) * n * (m - 1)
    f += (data[-2] - data[0]) * (n - 1)

    s = (data[-1] - data[0]) * n * (m - 1)
    s += (data[-1] - data[1]) * (n - 1)

    print(max(f, s))
