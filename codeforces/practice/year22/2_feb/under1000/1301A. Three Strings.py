for _ in range(int(input())):
    a = input()
    b = input()
    c = input()

    flag = True
    for i in range(len(a)):
        if c[i] != a[i] and c[i] != b[i]:
            flag = False
            break

    print("YES" if flag else "NO")