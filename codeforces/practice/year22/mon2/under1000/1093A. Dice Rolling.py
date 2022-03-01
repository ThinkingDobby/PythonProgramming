import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    print(x // 7 + (1 if x % 7 != 0 else 0))