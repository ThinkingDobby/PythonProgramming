for _ in range(int(input())):
    f = set(input())
    s = set(input())
    if f & s:
        print("YES")
    else:
        print("NO")