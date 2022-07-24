import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

tot = 0


def rec(lev, typ, cnt):
    global tot

    if lev > 1:
        if typ == 'r':
            rec(lev - 1, 'r', cnt)
            rec(lev, 'b', cnt * x)
        else:
            rec(lev - 1, 'r', cnt)
            rec(lev - 1, 'b', cnt * y)
    else:
        if typ == 'b':
            tot += cnt
        return


rec(n, 'r', 1)
print(tot)