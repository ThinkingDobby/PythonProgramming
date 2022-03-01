import sys

input = sys.stdin.readline

n = int(input())
tmp = set(list(map(int, input().split()))[1:])
for _ in range(n - 1):
    data = set(list(map(int, input().split()))[1:])
    tmp &= data

print(*tmp)