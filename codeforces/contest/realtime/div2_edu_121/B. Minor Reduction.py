for _ in range(int(input())):
    data = list(map(int, input()))
    flag = False
    idx = -1
    for i in range(1, len(data)):
        if data[i] + data[i - 1] > 9:
            flag = True
            idx = i

    if not flag:
        print(data[0] + data[1], end='')
        for i in range(2, len(data)):
            print(data[i], end='')
    else:
        for i in range(len(data)):
            if i == idx - 1:
                continue
            elif i == idx:
                print(data[idx - 1] + data[idx], end='')
            else:
                print(data[i], end='')

    print()