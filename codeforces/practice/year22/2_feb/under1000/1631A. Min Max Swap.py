for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mva = 0
    mvb = 0
    for i in range(n):
        if a[i] > b[i]:
            mva = max(mva, a[i])
            mvb = max(mvb, b[i])
        else:
            mva = max(mva, b[i])
            mvb = max(mvb, a[i])

    print(mva * mvb)