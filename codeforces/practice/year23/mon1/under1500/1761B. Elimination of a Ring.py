import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = set(map(int, input().split()))

    print(n if len(data) != 2 else n // 2 + 1)
