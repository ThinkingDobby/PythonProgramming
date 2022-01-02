x, y = list(input())
x = ord(x) - 96
y = int(y)

data = []
data.append((x + 2, y + 1))
data.append((x + 2, y - 1))
data.append((x - 2, y + 1))
data.append((x - 2, y - 1))
data.append((x + 1, y + 2))
data.append((x + 1, y - 2))
data.append((x - 1, y + 2))
data.append((x - 1, y - 2))

cnt = 0
for i in data:
    if 1 <= i[0] <= 8 and 1 <= i[1] <= 8:
        cnt += 1

print(cnt)