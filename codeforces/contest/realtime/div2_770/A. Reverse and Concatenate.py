for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(input())
    if k == 0:
        print(1)
    else:
        if data == data[::-1]:
            print(1)
        else:
            print(2)