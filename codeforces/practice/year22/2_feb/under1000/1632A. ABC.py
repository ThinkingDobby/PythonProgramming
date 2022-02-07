for _ in range(int(input())):
    n = int(input())
    data = input()
    if n > 2:
        print("NO")
    else:
        if n == 2 and data[0] == data[1]:
            print("NO")
        else:
            print("YES")