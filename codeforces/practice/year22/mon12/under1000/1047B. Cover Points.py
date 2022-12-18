import sys

input = sys.stdin.readline

tmp = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: sum(x))

print(sum(tmp[-1]))