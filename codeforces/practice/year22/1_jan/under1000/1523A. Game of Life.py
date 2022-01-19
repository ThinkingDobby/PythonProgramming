for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input()))

    data = [0] + data + [0]
    cnt = m
    while cnt:
        ndata = data[:]
        change = False
        for i in range(1, n + 1):
            if data[i - 1] + data[i + 1] == 1:
                ndata[i] = 1
                if data[i] == 0:
                    change = True

        if change:
            data = ndata[:]
        else:
            break
        cnt -= 1

    print("".join(map(str, data[1:-1])))
