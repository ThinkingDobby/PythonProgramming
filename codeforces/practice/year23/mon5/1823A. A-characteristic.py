import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    chk = False
    ans = -1
    for i in range(1, n + 1):
        if i * (i - 1) // 2 + (n - i) * (n - i - 1) // 2 == k:
            chk = True
            ans = i
            break

    if not chk:
        print("NO")
    else:
        print("YES")
        print(*([1] * ans + [-1] * (n - ans)))