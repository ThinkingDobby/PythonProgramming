import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if n % 2 == 1 and ((i == n // 2 and (j == 0 or j == n - 1)) or (j == n // 2 and (i == 0 or i == n - 1))):
                print(1, end=' ')
            elif i == j or n - i - 1 == j:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()
