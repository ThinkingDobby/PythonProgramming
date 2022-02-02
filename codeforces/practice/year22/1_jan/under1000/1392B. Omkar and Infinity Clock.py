for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    mv = max(data)
    tmp = [mv - i for i in data]
    mv = max(tmp)
    tmp2 = [mv - i for i in tmp]

    if k % 2 == 0:
        print(*tmp2)
    else:
        print(*tmp)