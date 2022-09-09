import sys

input = sys.stdin.readline

for _ in range(int(input())):
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = True
    for i in range(3):
        if a[i] > c[i]:
            ans = False
            break
        c[i] -= a[i]

    t1 = min(c[0], a[3])
    t2 = min(c[1], a[4])
    if c[2] - (a[3] - t1 + a[4] - t2) < 0:
        ans = False

    print("YES" if ans else "NO")