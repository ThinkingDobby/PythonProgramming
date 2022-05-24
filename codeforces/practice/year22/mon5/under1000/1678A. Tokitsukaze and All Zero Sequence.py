import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if 0 not in data:
        if len(set(data)) == n:
            print(n + 1)
        else:
            print(n)
    else:
        print(len([i for i in data if i != 0]))
