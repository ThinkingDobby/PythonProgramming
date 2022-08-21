import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, b, s = map(int, input().split())

    if 0 <= s - b * k <= (k - 1) * n:
        cnt = (s - b * k) // (k - 1) if k != 1 else 0
        rest = (s - b * k) % (k - 1) if k != 1 else 0

        memo = [0] * n
        for i in range(n):
            if cnt > 0:
                memo[i] += k - 1
                cnt -= 1
            elif cnt == 0:
                memo[i] += rest
                cnt -= 1

            if i == n - 1:
                memo[i] += b * k
        print(*memo)
    else:
        print(-1)



    # value = s // n
    # rest = s % n
    # svalue = value // k
    # srest = value % k
    #
    # base = svalue * n
    # trest = rest + srest * n
    # # base = svalue * (n - rest) + (1 + value) // k * rest
    # # trest = srest * (n - rest) + (1 + value) % k * rest
    # if base <= b <= base + trest // k:
    #     cnt = b - base
    #     print(cnt, base, trest)
    # else:
    #     print(-1)