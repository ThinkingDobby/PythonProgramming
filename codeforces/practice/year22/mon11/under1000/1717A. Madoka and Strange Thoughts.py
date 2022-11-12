import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    print(n + (n // 2 + n // 3) * 2)
