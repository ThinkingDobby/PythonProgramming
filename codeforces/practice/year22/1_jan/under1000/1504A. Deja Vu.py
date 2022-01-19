for _ in range(int(input())):
    data = list(input())

    flag = False
    for i in range(len(data)):
        if data[i] != 'a':
            if i == 0:
                data.append('a')
                flag = True
                break
            else:
                data.insert(len(data) - i, 'a')
                flag = True
                break

    if flag:
        print("YES")
        print("".join(data))
    else:
        print("NO")