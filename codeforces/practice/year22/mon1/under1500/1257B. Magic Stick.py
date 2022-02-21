for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= y:
        print("YES")
    else:
        if x > 3:
            print("YES")
        else:
            if x == 2 and y == 3:
                print("YES")
            else:
                print("NO")