for _ in range(int(input())):
    data = input()

    ans = ""
    flag = False

    i = 0
    while i < len(data):
        if i > 0:
            if data[i - 1] == data[i] and data[i] != '?':
                flag = True
                break

        if data[i] == '?':
            target = len(data)
            last = 'a'

            if i < len(data) - 1:
                for j in range(i + 1, len(data)):
                    if data[j] != '?':
                        target = j
                        last = data[j]
                        break
            else:
                if data[i] == 'a':
                    last = 'b'

            f = ''
            s = ''
            if i > 0:
                now = data[i - 1]
                if now == last:
                    if now == 'a':
                        f = 'b'
                        s = 'c'
                    elif now == 'b':
                        f = 'a'
                        s = 'c'
                    else:
                        f = 'a'
                        s = 'b'
                else:
                    tmp = ['a', 'b', 'c']
                    tmp.remove(now)
                    tmp.remove(last)
                    f = tmp[0]
                    s = now
            else:
                tmp = ['a', 'b', 'c']
                tmp.remove(last)
                f = tmp[0]
                s = tmp[1]

            t = 0
            for j in range(i, target):
                ans += f if t % 2 == 0 else s
                t += 1
            i = target
            continue

        else:
            ans += data[i]

        i += 1

    if flag:
        print(-1)
    else:
        print(ans)