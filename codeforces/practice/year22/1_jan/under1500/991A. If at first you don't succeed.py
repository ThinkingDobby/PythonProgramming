a, b, c, n = map(int, input().split())
tmp = n - (a + b - c)
if tmp < 1 or a < c or b < c:
    print(-1)
else:
    print(tmp)