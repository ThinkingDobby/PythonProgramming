for _ in range(int(input())):
    data = input()
    fcnt = 0
    scnt = 0
    cnt = 0
    for i in data:
        if i == '(':
            fcnt += 1
        elif i == ')':
            if fcnt > 0:
                fcnt -= 1
                cnt += 1
        elif i == '[':
            scnt += 1
        else:
            if scnt > 0:
                scnt -= 1
                cnt += 1

    print(cnt)

