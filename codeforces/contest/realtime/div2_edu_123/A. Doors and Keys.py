import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input()
    r = False
    g = False
    b = False

    flag = True
    for i in data:
        if i == 'r':
            r = True
        elif i == 'g':
            g = True
        elif i == 'b':
            b = True

        if not r and i == 'R':
            flag = False

        if not g and i == 'G':
            flag = False

        if not b and i == 'B':
            flag = False

    if flag:
        print("YES")
    else:
        print("NO")