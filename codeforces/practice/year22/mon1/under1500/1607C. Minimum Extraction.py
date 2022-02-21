for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if n == 1:
        print(data[0])
    else:
        m = min(data)
        if m <= 0:
            data.remove(m)
            for i in range(len(data)):
                data[i] -= m

        sdata = sorted(data)
        s = 0
        mv = sdata[0]
        for i in range(len(sdata) - 1):
            s = sdata[i]
            mv = max(mv, sdata[i + 1] - s)
        print(mv)
