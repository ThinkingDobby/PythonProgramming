import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(i + 1):
            print(0 if j != 0 and j != i else 1, end=' ')
        print()
