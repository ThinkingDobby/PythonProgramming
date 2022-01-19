for _ in range(int(input())):
    n, k = map(int, input().split())
    if k > (n + 1) // 2 - 1:
        print(-1)
    else:
        cnt = k
        for i in range(1, n - k + 1):
            print(i, end=' ')
            if cnt:
                print(n - cnt + 1, end=' ')
                cnt -= 1
        print()