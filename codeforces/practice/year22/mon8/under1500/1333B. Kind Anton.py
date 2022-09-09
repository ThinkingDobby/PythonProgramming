import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    f = False
    s = False

    ans = True
    for i in range(n):
        if a[i] > b[i] and not s:
            ans = False
            break
        elif a[i] < b[i] and not f:
            ans = False
            break

        if a[i] == 1:
            f = True
        if a[i] == -1:
            s = True

    print("YES" if ans else "NO")
