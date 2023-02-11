import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

x = 0
y = 0

px = 0
py = 0

cnt = 0
for i in range(n):

    if data[i] == 'U':
        y += 1
    elif data[i] == 'R':
        x += 1

    if (px > py and x < y) or (px < py and x > y):
        cnt += 1

    if x != y:
        px = x
        py = y

print(cnt)