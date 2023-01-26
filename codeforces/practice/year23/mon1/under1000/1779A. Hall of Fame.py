import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    chk_r = False
    chk_l = False
    ans = False
    idx = -1

    for i in range(n):
        if data[i] == 'R':
            chk_r = True
        elif data[i] == 'L':
            if chk_r:
                ans = True
            chk_l = True
            if i != n - 1 and data[i + 1] == 'R' and idx == -1:
                idx = i

    if ans:
        print("0")
    elif chk_r and chk_l:
        print(idx + 1)
    else:
        print("-1")