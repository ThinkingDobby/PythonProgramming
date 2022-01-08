for _ in range(int(input())):
    n, k = map(int, input().split())
    if (n + 1) // 2 < k:
        print(-1)
    else:
        for i in range(n):
            for j in range(n):
                if i == j and i % 2 == 0 and k != 0:
                    print('R', end='')
                    k -= 1
                else:
                    print('.', end='')
            print()
