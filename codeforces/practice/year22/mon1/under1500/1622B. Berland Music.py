for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    like = list(map(int, input()))

    a = set()
    b = set()
    cnt = like.count(1)

    for i in range(n):
        if like[i] == 1 and p[i] < n - cnt + 1:
            a.add(p[i])
        elif like[i] == 0 and p[i] >= n - cnt + 1:
            b.add(p[i])

    for i in range(n):
        if like[i] == 1 and p[i] < n - cnt + 1:
            print(b.pop(), end=' ')
        elif like[i] == 0 and p[i] >= n - cnt + 1:
            print(a.pop(), end=' ')
        else:
            print(p[i], end=' ')
    print()

