for _ in range(int(input())):
    n = int(input())
    data = input()
    if '8' in data:
        if n - data.index('8') >= 11:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")