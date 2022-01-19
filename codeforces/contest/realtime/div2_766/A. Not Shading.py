for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    r -= 1
    c -= 1
    data = [list(input()) for _ in range(n)]

    if data[r][c] == 'B':
        print(0)
    else:
        flag = False
        for i in range(m):
            if data[r][i] == 'B':
                flag = True
                break
        for i in range(n):
            if data[i][c] =='B':
                flag = True
                break

        if flag:
            print(1)
        else:
            chk = False
            for i in range(n):
                if 'B' in data[i]:
                    chk = True
                    break

            if chk:
                print(2)
            else:
                print(-1)