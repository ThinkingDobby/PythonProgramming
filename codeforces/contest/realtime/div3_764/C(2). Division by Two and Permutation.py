for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = [0] * (n + 1)

    for i in range(n):
        tmp = data[i]
        flag = True
        while tmp:
            if tmp <= n:
                for j in range(n, 0, -1):
                    if memo[j] == 0 and tmp == j:
                        memo[j] = 1
                        flag = False
                if not flag:
                    break
            tmp //= 2

    if all(memo[1:]):
        print("YES")
    else:
        print("NO")