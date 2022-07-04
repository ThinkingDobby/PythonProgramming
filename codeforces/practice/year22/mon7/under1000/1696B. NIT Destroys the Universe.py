import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    f = -1
    s = -1

    tmp = [0] + data
    for i in range(1, n + 1):
        if tmp[i - 1] == 0 and tmp[i] == 0:
            f = i - 1
        else:
            break

    tmp = data + [0]
    for i in range(n - 1, -1, -1):
        if tmp[i + 1] == 0 and tmp[i] == 0:
            s = i
        else:
            break

    if f == s:
        if f == s == 0:
            print(0)
        elif 0 in data:
            print(2)
        else:
            print(1)
    else:
        if f == -1 and s != -1:
            tmp = data[:s]
            if 0 in tmp:
                print(2)
            else:
                print(1)
        elif f != -1 and s == -1:
            tmp = data[f + 1:]
            if 0 in tmp:
                print(2)
            else:
                print(1)
        elif f >= s:
            print(0)
        else:
            tmp = data[f + 1:s]
            if 0 in tmp:
                print(2)
            else:
                print(1)
