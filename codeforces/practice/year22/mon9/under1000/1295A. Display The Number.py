import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    print('1' * (n // 2) if n % 2 == 0 else '7' + '1' * (n // 2 - 1))
