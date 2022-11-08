import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = set(input().rstrip())
    data |= set(input().rstrip())

    print(len(data) - 1)
