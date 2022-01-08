for _ in range(int(input())):
    data = list(input())
    ans = []

    if len(data) == 1:
        print(data[0])
    else:
        cnt = 1
        for i in range(1, len(data)):
            if data[i - 1] == data[i]:
                cnt += 1
            else:
                if cnt % 2 == 1:
                    ans.append(data[i - 1])
                cnt = 1

        if cnt % 2 == 1:
            ans.append(data[-1])

        print(''.join(sorted(set(ans))))