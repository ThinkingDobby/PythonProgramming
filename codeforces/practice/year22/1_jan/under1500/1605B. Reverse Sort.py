for _ in range(int(input())):
    n = int(input())
    data = input()

    memo = []
    for i in range(n):
        if data[i] == '1':
            memo.append(i + 1)

    ans = []
    now = 0
    for i in range(n - 1, n - 1 - len(memo), -1):
        if data[i] == '0':
            ans.append(memo[now])
            now += 1
            ans.append(i + 1)

    if len(ans) == 0:
        print(0)
    else:
        print(1)
        print(len(ans), *sorted(ans))
