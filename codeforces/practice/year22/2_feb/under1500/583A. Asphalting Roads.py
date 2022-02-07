n = int(input())
data = [list(map(int, input().split())) for _ in range(n * n)]

rchk = [False] * (n + 1)
cchk = [False] * (n + 1)
for i in range(n * n):
    if not rchk[data[i][0]] and not cchk[data[i][1]]:
        rchk[data[i][0]] = True
        cchk[data[i][1]] = True
        print(i + 1, end=' ')
