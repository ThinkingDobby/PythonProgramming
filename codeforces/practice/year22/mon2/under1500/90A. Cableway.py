r, g, b = map(int, input().split())

rc = ((r + 1) // 2 - 1) * 3 + 0
gc = ((g + 1) // 2 - 1) * 3 + 1
bc = ((b + 1) // 2 - 1) * 3 + 2

print(30 + max(rc, gc, bc))