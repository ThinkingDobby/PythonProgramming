import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = int(input())
    x = bin(data)[2:]

    if x.count('1') == 1:
        if data == 1:
            print(3)
        else:
            print(data + 1)
    else:
        tmp = x[::-1]
        for i in range(len(x)):
            if tmp[i] == '1':
                print(int('1' + '0' * i, 2))
                break
                