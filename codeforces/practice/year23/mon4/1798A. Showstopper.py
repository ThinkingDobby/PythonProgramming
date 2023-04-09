import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    f = max(a[-1], b[-1])
    s = min(a[-1], b[-1])

    ans = True
    for i in range(n):
        mav = max(a[i], b[i])
        miv = min(a[i], b[i])

        if mav > f or miv > s:
            ans = False
            break

    print("YES" if ans else "NO")
