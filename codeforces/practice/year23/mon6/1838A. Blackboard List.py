import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    print(data[0] if data[0] < 0 else data[-1])
