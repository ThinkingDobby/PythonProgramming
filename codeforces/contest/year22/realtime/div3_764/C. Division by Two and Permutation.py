import sys

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = [0] * (n + 1)
    memo2 = []
    for i in data:
        tmp = i
        tmp2 = []
        while tmp >= 1:
            if tmp <= n:
                memo[tmp] += 1
                tmp2.append(tmp)
            tmp //= 2
        memo2.append(tmp2)

    check = [0] * (n + 1)
    for i in range(n):
        mv = sys.maxsize
        idx = -1
        for j in memo2[i]:
            if memo[j] < mv and check[j] != 1:
                mv = memo[j]
                idx = j
            memo[j] -= 1
        if idx != -1:
            check[idx] = 1

    flag = True
    for i in check[1:]:
        if i != 1:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")