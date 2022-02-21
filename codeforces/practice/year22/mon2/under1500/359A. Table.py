n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

flag = False
for i in range(n):
    if data[i][0] == 1 or data[i][m - 1] == 1:
        flag = True
        break

for i in range(m):
    if data[0][i] == 1 or data[n - 1][i] == 1:
        flag = True
        break

if flag:
    print(2)
else:
    print(4)