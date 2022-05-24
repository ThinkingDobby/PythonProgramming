import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().rstrip()))

    if len(data) == 2:
        print(data[1])
    else:
        print(min(data))