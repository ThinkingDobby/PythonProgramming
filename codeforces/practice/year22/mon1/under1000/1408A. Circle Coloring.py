for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = [a[0]]
    for i in range(1, n - 1):
        for j in (a[i], b[i], c[i]):
            if j != ans[-1]:
                ans.append(j)
                break

    for i in (a[-1], b[-1], c[-1]):
        if i != ans[-1] and i != ans[0]:
            ans.append(i)
            break

    print(*ans)