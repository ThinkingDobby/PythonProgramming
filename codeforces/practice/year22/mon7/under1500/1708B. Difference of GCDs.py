import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, l, r = map(int, input().split())

    memo = []
    ans = True
    for i in range(1, n + 1):
        now = ((l + i - 1) // i) * i
        if now > r:
            ans = False
            break
        memo.append(now)

    if ans:
        print("YES")
        print(*memo)
    else:
        print("NO")