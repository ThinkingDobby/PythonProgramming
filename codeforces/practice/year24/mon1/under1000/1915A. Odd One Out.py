import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = sorted(map(int, input().split()))

    print(data[0] if data[0] != data[1] else data[2])