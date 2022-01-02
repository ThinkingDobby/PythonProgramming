for _ in range(int(input())):
    m = -1
    mn = ""
    for _ in range(int(input())):
        v, vn = input().split()
        if int(v) > m:
            m = int(v)
            mn = vn
    print(mn)