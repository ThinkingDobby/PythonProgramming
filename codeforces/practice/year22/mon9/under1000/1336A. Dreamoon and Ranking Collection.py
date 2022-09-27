import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    data = sorted(set(map(int, input().split())))

    memo = [False] * (max(data) + 1)
    for i in data:
        memo[i] = True

    rest = x
    ans = -1
    for i in range(1, len(memo)):
        if not memo[i] and rest:
            memo[i] = True
            rest -= 1
        if memo[i]:
            ans = i
        else:
            break

    if rest:
        ans += rest

    print(ans)