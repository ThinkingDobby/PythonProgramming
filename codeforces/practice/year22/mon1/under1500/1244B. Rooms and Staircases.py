for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input()))

    cnt = 0
    for i in range(n):
        if data[i] == 1:
            cnt = max(cnt, (i + 1) * 2, (n - i) * 2)

    print(max(cnt, n))