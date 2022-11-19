import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    print(min(sorted(data)[-2] - 1, n - 2))