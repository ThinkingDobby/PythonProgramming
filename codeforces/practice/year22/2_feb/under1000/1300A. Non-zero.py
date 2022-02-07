for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if data[i] == 0:
            data[i] = 1
            cnt += 1

    if sum(data) == 0:
        cnt += 1

    print(cnt)