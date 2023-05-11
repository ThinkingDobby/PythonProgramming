import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1:
        print(-1 if n != 1 else 1)
    else:
        for i in range(1, n, 2):
            print(i + 1, i, end=' ')
        print()
