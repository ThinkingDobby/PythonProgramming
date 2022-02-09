x, y = map(int, input().split())
m = -1 if (x > 0 and y > 0) or (x < 0 and y < 0) else 1


a = (0, -m * x + y)
b = (x - m * y, 0)
print(*a, *b) if a[0] < b[0] else print(*b, *a)