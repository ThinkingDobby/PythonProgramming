for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    memo = [b[i] - a[i] for i in range(n)]

    start = False
    end = False
    gap = -1
    flag = True

    for i in memo:
        if i < 0:
            flag = False
            break
        if i != 0:
            if not start:
                gap = i
            start = True
            if i != gap:
                flag = False
                break
        if start and i == 0:
            end = True
        if end and i != 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
