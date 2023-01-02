import sys

input = sys.stdin.readline

n = int(input())

data = [list(input().rstrip()) for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if data[i][j] == '.':
            if data[i - 1][j] == '.' and data[i][j - 1] == '.' and data[i + 1][j] == '.' and data[i][j + 1] == '.':
                data[i][j] = '#'
                data[i - 1][j] = '#'
                data[i][j - 1] = '#'
                data[i + 1][j] = '#'
                data[i][j + 1] = '#'

ans = True
for i in range(n):
    if '.' in data[i]:
        ans = False
        break

print("YES" if ans else "NO")