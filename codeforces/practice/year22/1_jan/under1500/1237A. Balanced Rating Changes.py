import math

n = int(input())
data = [int(input()) for _ in range(int(n))]

po = 0
no = 0

for i in range(n):
    if data[i] > 0 and data[i] % 2 == 1:
        po += 1
    elif data[i] < 0 and data[i] % 2 == 1:
        no += 1

if po > no:
    tmp = po - no
    f = True
    for i in range(n):
        if data[i] > 0 and data[i] % 2 == 1:
            if tmp:
                if f:
                    print(math.floor(data[i] / 2))
                    f = False
                else:
                    print(math.ceil(data[i] / 2))
                    f = True
                tmp -= 1
            else:
                print(math.floor(data[i] / 2))
        elif data[i] < 0 and data[i] % 2 == 1:
            print(math.ceil(data[i] / 2))
        else:
            print(data[i] // 2)
else:
    tmp = no - po
    f = True
    for i in range(n):
        if data[i] < 0 and data[i] % 2 == 1:
            if tmp:
                if f:
                    print(math.ceil(data[i] / 2))
                    f = False
                else:
                    print(math.floor(data[i] / 2))
                    f = True
                tmp -= 1
            else:
                print(math.ceil(data[i] / 2))
        elif data[i] > 0 and data[i] % 2 == 1:
            print(math.floor(data[i] / 2))
        else:
            print(data[i] // 2)