for _ in range(int(input())):
    data = input()
    if int(data[-1]) % 2 == 0:
        print(0)
    elif int(data[0]) % 2 == 0:
        print(1)
    elif [1 for i in data if int(i) % 2 == 0]:
        print(2)
    else:
        print(-1)
