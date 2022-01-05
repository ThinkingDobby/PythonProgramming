for _ in range(int(input())):
    n = int(input())
    data = input()
    sdata = sorted(data)

    chk = [0 if data[i] == sdata[i] else 1 for i in range(n)]
    if chk.count(1) == 0:
        print(0)
    else:
        print(1)
        print(chk.count(1), end=' ')
        for i in range(len(chk)):
            if chk[i] == 1:
                print(i + 1, end=' ')
        print()
