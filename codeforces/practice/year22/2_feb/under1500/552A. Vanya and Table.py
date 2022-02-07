s = 0

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    s += (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

print(s)