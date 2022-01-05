import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    a, b = map(int, inp().split())

    ans = sys.maxsize
    for i in range(40):
        if b == 1 and i == 0:
            continue
        cnt = i
        now = a

        while now:
            now //= (b + i)
            cnt += 1

        ans = min(ans, cnt)

    print(ans)
