import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    print(*([1] + [i for i in range(3, n + 1)] + [2]))