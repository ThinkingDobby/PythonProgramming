import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, t = map(int, input().split())

    print(max(s, t) - ((s + t) - n) + 1)
