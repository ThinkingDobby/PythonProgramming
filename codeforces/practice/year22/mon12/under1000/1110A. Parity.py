import sys

input = sys.stdin.readline

b, k = map(int, input().split())
data = list(map(int, input().split()))

ocnt = 0 if data[k - 1] % 2 == 0 else 1
fo = b % 2 == 1

if fo:
    for i in range(k - 1):
        if data[i] % 2 == 1:
            ocnt += 1

print("odd" if ocnt % 2 == 1 else "even")
