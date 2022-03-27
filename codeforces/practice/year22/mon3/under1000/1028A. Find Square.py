import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

sl = -1
el = -1
sh = -1
eh = -1

for i in range(n):
    for j in range(m):
        if data[i][j] == 'B':
            if sl == -1:
                sl = el = i + 1
                sh = eh = j + 1
            else:
                el = i + 1
                eh = j + 1

print((sl + el) // 2, (sh + eh) // 2)