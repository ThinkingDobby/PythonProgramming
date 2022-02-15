import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    flag = True

    modd = -1
    meven = -1
    for i in range(n):
        if data[i] % 2 == 0:
            if meven == -1:
                meven = data[i]
            else:
                if meven > data[i]:
                    flag = False
                    break
            meven = max(meven, data[i])
        else:
            if modd == -1:
                modd = data[i]
            else:
                if modd > data[i]:
                    flag = False
                    break
            modd = max(modd, data[i])

    if flag:
        print("Yes")
    else:
        print("No")