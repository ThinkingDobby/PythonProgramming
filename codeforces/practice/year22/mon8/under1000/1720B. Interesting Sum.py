import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))
    print(sum(data[-2:]) - sum(data[:2]))
