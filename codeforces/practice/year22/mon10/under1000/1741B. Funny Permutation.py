import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    if n == 3:
        print(-1)
    else:
        print(*[n, n - 1] + [i for i in range(1, n - 1)])
