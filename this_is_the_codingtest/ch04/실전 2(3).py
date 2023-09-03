import sys

input = sys.stdin.readline

data = input().rstrip()

dirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

r = int(data[1]) - 1
c = ord(data[0]) - 97

cnt = 0
for a, b in dirs:
    if 0 <= r + a < 8 and 0 <= c + b < 8:
        cnt += 1

print(cnt)