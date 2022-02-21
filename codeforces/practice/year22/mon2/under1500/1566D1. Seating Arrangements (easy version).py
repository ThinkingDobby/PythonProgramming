import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sa = sorted(a)
    memo = [False] * m

    cnt = 0
    for i in range(m):
        idx = -1
        for j in range(m):
            if a[i] == sa[j]:
                idx = j
            if a[i] < sa[j]:
                break

        cnt += memo[:idx].count(True)
        memo[idx] = True
        sa[idx] = -1

    print(cnt)