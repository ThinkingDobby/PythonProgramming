import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, q = map(int, input().split())
    data = list(map(int, input().split())) + [q + 1]

    memo = []
    prev = -1
    check = False
    for i in range(n):
        if data[i] <= q:
            if not check:
                prev = i
                check = True
            if check and data[i + 1] > q:
                memo.append(i - prev + 1)
                check = False

    ans = 0
    for s in memo:
        tmp = max(0, s - k + 1)
        ans += tmp * (tmp + 1) // 2

    print(ans)
