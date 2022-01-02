for t in range(int(input())):
    n, l, r, k = map(int, input().split(" "))
    a = sorted(list(map(int, input().split(" "))))
    memo = []
    for i in a:
        if l <= i <= r:
            memo.append(i)

    sum = 0
    ans = False
    for i in range(len(memo)):
        if sum + memo[i] > k:
            print(i)
            ans = True
            break
        sum += memo[i]
    if not ans:
        print(len(memo))