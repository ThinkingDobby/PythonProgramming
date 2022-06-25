import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    print(max(0, sum(data) - m))