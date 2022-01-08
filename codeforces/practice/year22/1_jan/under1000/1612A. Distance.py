for _ in range(int(input())):
    x, y = map(int, input().split(" "))
    if (x + y) % 2 == 1:
        print(-1, -1)
    else:
        if x > y:
            print((x - y) // 2, y)
        else:
            print(x, (y - x) // 2)