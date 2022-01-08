for _ in range(int(input())):
    n, k = map(int, input().split())
    sdata = sorted(map(lambda x: n - int(x), input().split()))

    s = 0
    cnt = 0
    for i in sdata:
        if s + i <= n - 1:
            s += i
            cnt += 1

    print(cnt)