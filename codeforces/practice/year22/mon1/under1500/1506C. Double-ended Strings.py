for _ in range(int(input())):
    a = input()
    b = input()

    ls = a if len(a) > len(b) else b
    ss = b if len(a) > len(b) else a

    flag = False
    ans = len(ls) + len(ss)
    for l in range(len(ss), 0, -1):
        for j in range(len(ss)):
            if j + l > len(ss):
                break
            if ss[j:j + l] in ls:
                flag = True
                ans = len(ls) - l + len(ss) - l
                break
        if flag:
            break

    print(ans)
