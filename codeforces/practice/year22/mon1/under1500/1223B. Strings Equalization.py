for _ in range(int(input())):
    s = input()
    t = input()

    flag = False
    if len(s) == 1:
        if s == t:
            flag = True
    else:
        for i in range(len(s)):
            if s[i] in t:
                flag = True
                break

    if flag:
        print("YES")
    else:
        print("NO")
