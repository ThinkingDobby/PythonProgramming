import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    memo = [i for i in range(1, k + 1)] + [i for i in range(n, k, - 1)]
    print(*memo)