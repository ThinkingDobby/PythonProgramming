import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(*[2 * i for i in range(1, n + 1)])
