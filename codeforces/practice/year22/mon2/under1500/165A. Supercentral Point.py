data = [list(map(int, input().split())) for i in range(int(input()))]
xmemo = {}
ymemo = {}

for x, y in data:
    if x in xmemo:
        xmemo[x][0] = max(xmemo[x][0], y)
        xmemo[x][1] = min(xmemo[x][1], y)
    else:
        xmemo[x] = [y, y]

    if y in ymemo:
        ymemo[y][0] = max(ymemo[y][0], x)
        ymemo[y][1] = min(ymemo[y][1], x)
    else:
        ymemo[y] = [x, x]

cnt = 0
for x, y in data:
    if xmemo[x][1] < y < xmemo[x][0] and ymemo[y][1] < x < ymemo[y][0]:
        cnt += 1

print(cnt)