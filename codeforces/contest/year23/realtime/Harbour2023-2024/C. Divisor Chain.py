import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())

    ans = []
    now = 1

    while now < x:
        ans.append(now)
        now *= 2

    rest = x - ans[-1]
    check = rest % 2
    rest -= check

    last = ans[-1]
    for i in range(31, -1, -1):
        tmp = rest & 2**i
        if tmp:
            last += 2**i
            ans.append(last)

    if check:
        ans.append(x)

    print(len(ans))
    print(*reversed(ans))
