m = int(input())
c = list(map(int, input().split()))
x, y = map(int, input().split())

s = 0
idx = -1
for i in range(m):
    s += c[i]
    if x <= s <= y and x <= sum(c) - s <= y:
        idx = i
        break

if idx == -1 or idx == m - 1:
    print(0)
else:
    print(idx + 2)