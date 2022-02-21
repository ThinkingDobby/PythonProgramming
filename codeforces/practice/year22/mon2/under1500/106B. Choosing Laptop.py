import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) + [i + 1] for i in range(n)]
sdata = sorted(data, key=lambda x:x[3])

ans = sdata[-1][4]
for i in range(n - 1):
    flag = True
    for j in range(i + 1, n):
        tmp = False
        for k in range(3):
            if sdata[i][k] >= sdata[j][k]:
                tmp = True
        if not tmp:
            flag = False
    if flag:
        ans = sdata[i][4]
        break

print(ans)
