for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    memo = {}

    m = -1
    for i in range(n):
        if data[i] in memo:
            tmp = memo[data[i]][1]
            m = max(m, tmp + n - i)
            memo[data[i]] = [tmp, i]
        else:
            memo[data[i]] = [i, i]

    print(m)