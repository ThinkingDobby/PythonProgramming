x, y = list(input())
x = ord(x) - 96
y = int(y)

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

cnt = 0
for step in steps:
    if 1 <= x + step[0] <= 8 and 1 <= y + step[1] <= 8:
        cnt += 1
print(cnt)