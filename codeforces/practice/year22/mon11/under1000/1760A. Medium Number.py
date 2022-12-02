import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = sorted(map(int, input().split()))
    print(data[1])
