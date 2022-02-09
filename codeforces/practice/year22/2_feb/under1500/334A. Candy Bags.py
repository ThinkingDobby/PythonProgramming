n = int(input())
for i in range(n):
    flag = True
    now = i + 1
    while now <= n * n:
        print(now, end=' ')
        if flag:
            now += (n - (i + 1)) * 2 + 1
        else:
            now += i * 2 + 1
        flag = True if not flag else False

    print()