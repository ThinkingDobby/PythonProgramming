import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(n):
    if k in range(data[i][0], data[i][1] + 1):
        print(n - i)
        break
