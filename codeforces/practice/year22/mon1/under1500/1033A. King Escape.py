n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

fx = bx if cx > bx else cx
sx = cx if cx > bx else bx
fy = by if cy > by else cy
sy = cy if cy > by else by

if ax in range(fx, sx + 1) or ay in range(fy, sy + 1):
    print("NO")
else:
    print("YES")