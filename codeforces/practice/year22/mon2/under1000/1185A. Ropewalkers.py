a, b, c, d = map(int, input().split())
tmp = sorted([a, b, c])
ans = max(0, d - (tmp[1] - tmp[0])) + max(0, d - (tmp[2] - tmp[1]))
print(ans)