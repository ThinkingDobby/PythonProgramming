import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    for i in range(n, (n + 1) // 2, -1):
        print(i - n // 2, i, end=' ')

    print("" if n % 2 == 0 else "1")