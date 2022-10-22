import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print((n - 3) // 3 - 1)