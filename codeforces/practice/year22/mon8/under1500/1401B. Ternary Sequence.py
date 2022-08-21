import sys

input = sys.stdin.readline

for _ in range(int(input())):
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))

    ans = 0

    tmp = min(f[2], s[1])
    f[2] -= tmp
    s[1] -= tmp
    ans += tmp * 2

    for i in range(3):
        if not f[2]:
            break
        tmp = min(f[2], s[2 - i])
        f[2] -= tmp
        s[2 - i] -= tmp

    for i in range(3):
        if not f[0]:
            break
        tmp = min(f[0], s[2 - i])
        f[0] -= tmp
        s[2 - i] -= tmp

    for i in range(3):
        if not f[1]:
            break
        tmp = min(f[1], s[2 - i])
        f[1] -= tmp
        s[2 - i] -= tmp
        if i == 0:
            ans -= tmp * 2

    print(ans)