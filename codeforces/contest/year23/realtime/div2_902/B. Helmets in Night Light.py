import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, p = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    memo = sorted(list(zip(a, b)) + [(n, p)], key=lambda x: x[1])

    cost = p
    cnt = n - 1

    for i in range(len(memo)):
        if cnt <= 0:
            break
        tmp = min(cnt, memo[i][0])
        cost += tmp * memo[i][1]
        cnt -= tmp

        if cnt <= 0:
            break

    print(cost)