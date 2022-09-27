import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1:
        print(1, end=' ')

    for i in range(n - 2, 0, -1):
        if n % 2 == 1 and i == 1:
            break
        print(i, end=' ')

    print(n - 1, n)
