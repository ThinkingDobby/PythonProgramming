import sys

input = sys.stdin.readline

n = int(input())
print((n * n + 2 - 1) // 2)
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('C', end='')
        else:
            print('.', end='')
    print()

