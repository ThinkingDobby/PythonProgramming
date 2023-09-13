import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = input().split()

    if len(l) > len(r):
        r = '0' * (len(l) - len(r)) + r
    else:
        l = '0' * (len(r) - len(l)) + l

    cnt = 0
    final = len(l)
    for i in range(len(l)):
        if int(l[i]) != int(r[i]):
            final = i
            break

    if final == len(l):
        ans = 0
    else:
        ans = abs(int(l[final]) - int(r[final])) + (len(l) - final - 1) * 9

    print(ans)
