for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())

    la = len(str(x1)) + p1
    lb = len(str(x2)) + p2

    if la > lb:
        print('>')
    elif la < lb:
        print('<')
    else:
        a = str(x1)
        b = str(x2)
        if p1 > p2:
            a += '0' * (p1 - p2)
        elif p1 < p2:
            b += '0' * (p2 - p1)
        if int(a) > int(b):
            print('>')
        elif int(a) < int(b):
            print('<')
        else:
            print('=')
