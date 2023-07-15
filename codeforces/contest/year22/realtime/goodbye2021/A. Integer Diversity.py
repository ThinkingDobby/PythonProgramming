for t in range(int(input())):
    n = input()
    memo = [0 for _ in range(101)]
    a = list(map(int, input().split(" ")))
    for i in range(len(a)):
        if a[i] < 0: memo[-a[i]] += 1
        elif a[i] > 0: memo[a[i]] += 1
        else: memo[0] = 1
    sum = 0
    for i in range(len(memo)): sum += min(2, memo[i])
    print(sum)