n, m = map(int, input().split())

if m % n != 0:
    print(-1)
else:
    tmp = m // n
    cnt = 0
    while tmp % 2 == 0 and tmp >= 2:
        tmp //= 2
        cnt += 1
    while tmp % 3 == 0 and tmp >= 3:
        tmp //= 3
        cnt += 1
    if tmp != 1:
        print(-1)
    else:
        print(cnt)