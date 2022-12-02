import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    print(ord(sorted(data)[-1]) - 96)
