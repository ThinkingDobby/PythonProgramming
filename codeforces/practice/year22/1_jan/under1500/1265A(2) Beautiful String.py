for _ in range(int(input())):
    data = list(" " + input())
    l = {'a', 'b', 'c'}
    flag = False

    for i in range(1, len(data) - 1):
        if data[i] == '?':
            d = {data[i + 1], data[i - 1]}
            d = list(l - d - {'?'})
            data[i] = d[0]
        else:
            if data[i] == data[i + 1]:
                flag = True
                break

    if data[-1] == '?' and not flag:
        d = list(l - {data[-2]} - {'?'})
        data[-1] = d[0]
    if flag:
        print(-1)
    else:
        print("".join(data[1:]))