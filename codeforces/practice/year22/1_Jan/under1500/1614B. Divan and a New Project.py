for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    new = list(enumerate(data))
    memo = [0 for i in range(n)]

    sd = sorted(new, reverse=True, key=lambda x: x[1])

    fcnt = 1
    scnt = -1
    s = 0
    for i in range(n):
        if i % 2 == 0:
            memo[sd[i][0]] = fcnt
            s += fcnt * 2 * sd[i][1]
            fcnt += 1
        else:
            memo[sd[i][0]] = scnt
            s += -scnt * 2 * sd[i][1]
            scnt -= 1

    print(s)
    print(0, end=" ")
    for i in range(n):
        print(memo[i], end=" ")
    print()
