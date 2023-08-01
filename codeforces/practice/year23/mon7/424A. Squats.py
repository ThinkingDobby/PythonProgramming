import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())

cnt = data.count('X')
tmp = n // 2 - cnt

print(abs(tmp))
if tmp > 0:
    for i in range(n):
        if data[i] == 'x' and tmp > 0:
            tmp -= 1
            print('X', end='')
        else:
            print(data[i], end='')
else:
    tmp = -tmp
    for i in range(n):
        if data[i] == 'X' and tmp > 0:
            tmp -= 1
            print('x', end='')
        else:
            print(data[i], end='')