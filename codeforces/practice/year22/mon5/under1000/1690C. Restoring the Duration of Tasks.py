import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    fin = list(map(int, input().split()))

    print(fin[0] - start[0], end=' ')
    f = fin[0]
    for i in range(1, n):
        f = max(f, start[i], fin[i - 1])
        print(fin[i] - f, end=' ')
    print()