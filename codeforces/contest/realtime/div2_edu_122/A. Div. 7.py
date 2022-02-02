for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        for i in range(0, 10):
            tmp = int(str(n)[:-1] + str(i))
            if tmp % 7 == 0:
                print(tmp)
                break
