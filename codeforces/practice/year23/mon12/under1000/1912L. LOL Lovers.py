import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

lc = data.count('L')
oc = data.count('O')

nowl = nowo = 0

idx = -1
for i in range(n - 1):
    if data[i] == 'L':
        nowl += 1
    else:
        nowo += 1
    if nowl != lc - nowl and nowo != oc - nowo:
        idx = i
        break

print(idx + 1 if idx != -1 else -1)


