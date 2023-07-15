for _ in range(int(input())):
    n, l = map(int, input().split())
    data = list(map(lambda x:bin(int(x))[2:], input().split()))

    memo = [0] * l

    for i in data:
        for j in range(1, len(i) + 1):
            if i[-j] == '1':
                memo[-j] += 1
            else:
                memo[-j] -= 1
        for j in range(len(i) + 1, l + 1):
            memo[-j] -= 1

    ans = ''
    for i in range(1, l + 1):
        if memo[-i] > 0:
            ans += '1'
        else:
            ans += '0'

    print(int(ans[::-1], 2))
