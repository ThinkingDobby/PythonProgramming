import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())
al = set(map(int, input().split()))
bl = set(map(int, input().split()))

tl = bl - al
for i in range(1, n + 1):
    if i in al:
        print(1, end=' ')
    elif i in bl:
        print(2, end=' ')