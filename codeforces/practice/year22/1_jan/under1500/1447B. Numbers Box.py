import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n, m = map(int, inp().split())

    data = [list(map(int, inp().split())) for i in range(n)]

    zero = False
    min_abs = sys.maxsize
    cnt = 0
    s = 0
    for i in range(n):
        for j in range(m):
            tmp = data[i][j]
            min_abs = min(min_abs, abs(tmp))
            if tmp < 0:
                cnt += 1
                s += -tmp
            elif tmp > 0:
                s += tmp
            else:
                zero = True

    if zero or cnt % 2 == 0:
        print(s)
    else:
        print(s - 2 * min_abs)
