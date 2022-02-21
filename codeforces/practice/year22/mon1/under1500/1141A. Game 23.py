n, m = map(int, input().split())

if m % n != 0 or (((m // n) % 2 != 0) and ((m // n) % 3 != 0)):
    if m == n:
        print(0)
    else:
        print(-1)
else:
    tmp = m
    cnt = 0
    while tmp % 2 == 0 and tmp >= 2:
        tmp //= 2
        cnt += 1
    while tmp % 3 == 0 and tmp >= 3:
        tmp //= 3
        cnt += 1

    tmp2 = n
    cnt2 = 0
    while tmp2 % 2 == 0 and tmp2 >= 2:
        tmp2 //= 2
        cnt2 += 1
    while tmp2 % 3 == 0 and tmp2 >= 3:
        tmp2 //= 3
        cnt2 += 1

    if tmp != tmp2:
        print(-1)
    else:
        print(cnt - cnt2)

