import sys

input = sys.stdin.readline

for _ in range(int(input())):
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    tx = [xb - xa, xc - xa]
    ty = [yb - ya, yc - ya]

    cnt = 1
    if tx[0] * tx[1] > 0:
        cnt += min(map(abs, tx))
    if ty[0] * ty[1] > 0:
        cnt += min(map(abs, ty))

    print(cnt)