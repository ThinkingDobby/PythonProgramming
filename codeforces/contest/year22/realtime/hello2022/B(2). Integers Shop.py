import sys
inp = sys.stdin.readline

INT_MAX = sys.maxsize

for _ in range(int(inp())):
    n = int(inp())
    d = {}
    ml = (INT_MAX, INT_MAX)
    mr = (0, -1)

    for i in range(n):
        l, r, c = map(int, inp().split())
        ml = min(ml, (l, c))
        mr = max(mr, (r, -c))
        d[(l, r)] = min(d.get((l, r), INT_MAX), c)
        print(min(ml[1] - mr[1], d.get((ml[0], mr[0]), INT_MAX)))