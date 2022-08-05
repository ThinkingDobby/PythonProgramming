import sys

input = sys.stdin.readline

n, m = map(int, input().split())
while True:
    chk = True
    for i in range(1, n + 1):
        if m >= i:
            m -= i
        else:
            chk = False
            break
    if not chk:
        break

print(m)