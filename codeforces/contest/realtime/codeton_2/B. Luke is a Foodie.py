import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    data = list(map(int, input().split()))

    l = data[0] - x
    r = data[0] + x
    cnt = 0
    for i in range(1, n):
        nl = data[i] - x
        nr = data[i] + x

        if nr < l or nl > r:
            cnt += 1
            l = nl
            r = nr
        else:
            l = max(nl, l)
            r = min(nr, r)

    print(cnt)
