import sys

input = sys.stdin.readline

p, n = map(int, input().split())
memo = set()

idx = -2
for i in range(n):
    data = int(input())
    if data % p in memo:
        idx = i
        break
    else:
        memo.add(data % p)

print(idx + 1)