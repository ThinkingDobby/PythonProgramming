import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    fcnt = scnt = 0
    fchk = schk = False

    for i in range(n):
        if not fchk and c[i] == c[0]:
            fcnt += 1
            if fcnt >= k:
                fchk = True

        if fchk and not schk and c[i] == c[-1]:
            scnt += 1
            if scnt >= k:
                schk = True

    if c[0] == c[-1]:
        print("YES" if fchk else "NO")
    else:
        print("YES" if schk else "NO")