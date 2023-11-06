import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    for i in range(n // 2):
        print(n - i, i + 1, end=' ')

    if n % 2 == 1:
        print((n + 1) // 2, end=' ')
    print()