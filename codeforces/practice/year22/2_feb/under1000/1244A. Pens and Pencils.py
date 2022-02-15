for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    x = (a + c - 1) // c
    y = (b + d - 1) // d
    if x + y > k:
        print(-1)
    else:
        print(x, y)