for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()), reverse=True)
    cnt = 0
    mv = -1
    for i in range(n):
        cnt += 1
        if cnt >= data[i]:
            mv = max(mv, data[i])
        else:
            mv = max(mv, cnt)

    print(mv)