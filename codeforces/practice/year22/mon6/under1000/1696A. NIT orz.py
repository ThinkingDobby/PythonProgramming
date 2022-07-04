import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, z = map(int, input().split())
    data = list(map(int, input().split()))

    mv = -1
    for i in data:
        mv = max(mv, z | i)
    print(mv)