for t in range(int(input())):
    n = input()
    a = input()
    str = a[0]
    ch = False
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            break
        if a[i] == a[i + 1] and ch == False:
            break
        else:
            ch = True
            str += a[i + 1]
    print(str + str[::-1])