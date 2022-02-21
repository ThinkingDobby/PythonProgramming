for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(input()) for i in range(n)]

    first = True
    case = True
    flag = True

    for i in range(n):
        for j in range(m):
            if first:
                if data[i][j] != '.':
                    if (data[i][j] == 'W' and (i + j) % 2 == 0) or (data[i][j] == 'R' and (i + j) % 2 == 1):
                        case = False
                    first = False
            else:
                if case:
                    if (data[i][j] == 'W' and (i + j) % 2 == 0) or (data[i][j] == 'R' and (i + j) % 2 == 1):
                        flag = False
                        break
                if not case:
                    if (data[i][j] == 'R' and (i + j) % 2 == 0) or (data[i][j] == 'W' and (i + j) % 2 == 1):
                        flag = False
                        break

    if flag:
        a = ''
        b = ''
        if case:
            a = 'R'
            b = 'W'
        else:
            a = 'W'
            b = 'R'
        print("YES")
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    print(a, end='')
                else:
                    print(b, end='')
            print()
    else:
        print("NO")
