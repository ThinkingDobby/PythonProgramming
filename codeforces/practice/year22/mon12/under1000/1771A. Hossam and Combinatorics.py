import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))
    f = data.count(data[0])
    s = data.count(data[-1])
    if data[0] == data[-1]:
        print(f * (s - 1))
    else:
        print(f * s * 2)