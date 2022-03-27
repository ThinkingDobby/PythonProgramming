import sys

input = sys.stdin.readline

n = int(input())
data = [[i, sum(map(int, input().split()))] for i in range(n)]
tmp = sorted(data, key=lambda x:(-x[1], x[0]))
for i in range(n):
    if tmp[i][0] == 0:
        print(i + 1)