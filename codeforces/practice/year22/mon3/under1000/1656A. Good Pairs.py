import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    print(data.index(min(data)) + 1, data.index(max(data)) + 1)