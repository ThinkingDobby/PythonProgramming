for _ in range(int(input())):
    n = int(input())
    data = list(input()) + ['A']
    flag = False if data[0] == 'P' else True
    mv = 0
    cnt = 0
    for i in range(1, n + 1):
        if data[i] == 'P':
            if flag:
                cnt += 1
        else:
            flag = True
            if data[i - 1] == 'P':
                mv = max(cnt, mv)
                cnt = 0

    print(mv)