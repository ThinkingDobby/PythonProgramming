import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, c, d = map(int, input().split())
    data = sorted(map(int, input().split()))

    print(*data)