for i in range(int(input())):
    a, b, c = map(int, input().split())
    tmp1 = min(b, c // 2)
    b -= tmp1
    tmp2 = min(a, b // 2)
    print(tmp1 * 3 + tmp2 * 3)
