n, k = map(int, input().split())
data = list(map(int, input()))

if n == 1:
    if k >= 1:
        print(0)
    else:
        print(data[0])
else:
    cnt = k
    if cnt > 0 and data[0] != 1:
        data[0] = 1
        cnt -= 1
    i = 1
    while cnt:
        if i >= n:
            break
        if data[i] != 0:
            data[i] = 0
            cnt -= 1
        i += 1

    print("".join(map(str, data)))