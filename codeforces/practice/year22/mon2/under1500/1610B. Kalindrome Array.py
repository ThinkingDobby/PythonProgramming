import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    f = -1
    s = -1
    flag = False

    for i in range((n + 1) // 2):
        if data[i] != data[n - i - 1]:
            f = data[i]
            s = data[n - i - 1]
            break

    if f != -1:
        tmp = [i for i in data if i != f]
        if tmp == tmp[::-1]:
            flag = True
        if not flag:
            tmp = [i for i in data if i != s]
            if tmp == tmp[::-1]:
                flag = True
    else:
        flag = True

    if flag:
        print("YES")
    else:
        print("NO")