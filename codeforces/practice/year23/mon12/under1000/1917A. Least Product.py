import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if 0 in data:
        print(0)
    elif len([i for i in data if i < 0]) % 2 == 0:
        print(1)
        print(1, 0)
    else:
        print(0)