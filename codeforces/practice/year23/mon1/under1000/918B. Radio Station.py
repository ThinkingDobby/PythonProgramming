import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()
for _ in range(n):
    data = input().split()
    memo[data[1]] = data[0]

for _ in range(m):
    data = input().split()
    print(data[0] + " " + data[1] + " #" + memo[data[1][:-1]])
