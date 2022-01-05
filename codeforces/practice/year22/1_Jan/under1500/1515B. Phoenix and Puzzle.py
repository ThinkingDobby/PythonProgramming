from math import *

for _ in range(int(input())):
    n = int(input())
    flag = False

    fs = sqrt(n / 2)
    if floor(fs) == fs:
        flag = True

    ss = sqrt(n / 4)
    if floor(ss) == ss:
        flag = True

    if flag:
        print("YES")
    else:
        print("NO")