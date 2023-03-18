import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    print(2 * max(abs(a), abs(b)) - (1 if abs(a) != abs(b) else 0))