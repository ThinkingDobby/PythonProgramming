import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    c, d = map(int, inp().split())

    if (c + d) % 2 == 1:
        print(-1)
    elif c == d == 0:
        print(0)
    elif abs(c) == abs(d):
        print(1)
    else:
        print(2)