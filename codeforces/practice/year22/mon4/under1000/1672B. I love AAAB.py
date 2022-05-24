import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    acnt = 0
    bcnt = 0
    flag = True
    if data[-1] != 'B':
        flag = False
    for i in data:
        if i == 'A':
            acnt += 1
        else:
            bcnt += 1
        if bcnt > acnt:
            flag = False
            break

    print("YES" if flag else "NO")