import sys

input = sys.stdin.readline

dirs = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}

n = int(input())
data = list(input().split())

now = [1, 1]
for i in data:
    if 0 < now[0] + dirs[i][0] <= n and 0 < now[1] + dirs[i][1] <= n:
        now[0] += dirs[i][0]
        now[1] += dirs[i][1]

print(*now)

"""
5
R R R U D D
"""