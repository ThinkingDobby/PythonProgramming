for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    now = False if data[0] == 0 else True
    cnt = 2 if now else 1
    die = False
    for i in range(1, n):
        if data[i] == 0:
            if not now:
                die = True
                break
            else:
                now = False
        else:
            if not now:
                cnt += 1
                now = True
            else:
                cnt += 5

    if die:
        print(-1)
    else:
        print(cnt)