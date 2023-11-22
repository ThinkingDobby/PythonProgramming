import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input().rstrip()
    b = input().rstrip()

    chk = True
    for i in range(1, m):
        if b[i] == b[i - 1]:
            chk = False

    ans = True
    for i in range(1, n):
        if a[i] == a[i - 1]:
            if not chk:
                ans = False
                break
            else:
                if a[i] == b[-1] or a[i - 1] == b[0]:
                    ans = False
                    break

    print("YES" if ans else "NO")
