import sys

input = sys.stdin.readline

k = int(input())
types = ["423131" * 2, "423141" * 2, "424231" * 2, "423231" * 2]

data = [list(map(int, input().split())) for _ in range(6)]

ntype = ''
for i in data:
    ntype += str(i[0])

t = -1
for i in range(4):
    if ntype in types[i]:
        t = i

idx = types[t].index(ntype)
data = data[-idx:] + data[:6 - idx]

ans = -1
if t == 0:
    ans = data[0][1] * data[0 + 1][1] - data[0 + 3][1] * data[0 + 4][1]
elif t == 1:
    ans = data[0 + 1][1] * data[0 + 2][1] - data[0 + 4][1] * data[0 + 5][1]
elif t == 2:
    ans = data[0 + 4][1] * data[0 + 5][1] - data[0 + 1][1] * data[0 + 2][1]
else:
    ans = data[0][1] * data[0 + 5][1] - data[0 + 2][1] * data[0 + 3][1]

print(ans * k)