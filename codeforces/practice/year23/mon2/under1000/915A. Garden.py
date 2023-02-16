import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = sorted(map(int, input().split()), reverse=True)

for i in range(n):
    if k % data[i] == 0:
        print(k // data[i])
        break
