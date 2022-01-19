for t in range(int(input())):
    if t != 0:
        input()
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.reverse()
    if max([a[i] + b[i] for i in range(n)]) <= x:
        print("Yes")
    else:
        print("No")