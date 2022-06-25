import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    f = m * (m - 1) // 2
    s = m * (n * (n + 1) // 2)
    print(f + s)