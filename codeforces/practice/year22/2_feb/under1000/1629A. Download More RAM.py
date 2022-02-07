for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    data = sorted(zip(a, b))

    now = k
    for i in range(n):
        if data[i][0] > now:
            break
        now += data[i][1]

    print(now)