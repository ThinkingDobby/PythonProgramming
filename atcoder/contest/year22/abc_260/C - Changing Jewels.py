import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

ans = [0]
def func(type, lev, cnt):
    if type == 'r':
        if lev >= 2:
            func('r', lev - 1, cnt)
            func('b', lev, x * cnt)
        elif lev == 1:
            return
    else:
        if lev > 2:
            func('r', lev - 1, cnt)
            func('b', lev - 1, y * cnt)
        elif lev == 2:
            ans[0] += cnt * y
            return
    return

func('r', n, 1)
print(*ans)

