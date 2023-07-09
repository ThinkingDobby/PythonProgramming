import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

check = [True for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            check[i] = False
        elif data[i][j] == 2:
            check[j] = False
        elif data[i][j] == 3:
            check[i] = False
            check[j] = False

tmp = [i + 1 for i in range(n) if check[i]]
print(len(tmp))
if tmp:
    print(*tmp)