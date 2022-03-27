import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(2**n - 1)