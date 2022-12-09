import sys

input = sys.stdin.readline

n, v = map(int, input().split())

if n - 1 < v:
    print(n - 1)
else:
    tot = v
    for i in range(2, n - v + 1):
        tot += i

    print(tot)
