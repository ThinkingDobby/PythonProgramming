for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = [-1 for i in range(n)]

    now = [i + 1 for i in range(n)]
    for t in range(n + 1):
        tmp = [0 for i in range(n)]
        for i in range(n):
            tmp[i] = now[data[i] - 1]
            if tmp[i] == i + 1 and memo[i] == -1:
                memo[i] = t + 1
        now = tmp

    print(" ".join(list(map(str, memo))))
