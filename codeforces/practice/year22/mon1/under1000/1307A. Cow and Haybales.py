for _ in range(int(input())):
    n, d = map(int, input().split())
    data = list(map(int, input().split()))

    s = 0
    cnt = d
    for i in range(1, n):
        if data[i] * i >= cnt:
            s += cnt // i
            break
        else:
            s += data[i]
            cnt -= data[i] * i

    print(data[0] + s)