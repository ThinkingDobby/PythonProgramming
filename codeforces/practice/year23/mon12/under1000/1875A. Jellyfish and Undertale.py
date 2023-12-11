import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    data = sorted(map(int, input().split()))

    now = b - 1
    for i in range(n):
        now += min(data[i], a - 1)

    print(now + 1)
