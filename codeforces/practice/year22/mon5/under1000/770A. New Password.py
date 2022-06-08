import sys

input = sys.stdin.readline

n, k = map(int, input().split())

for i in range(n):
    print(chr(i % k + 97), end='')