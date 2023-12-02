import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip().split("#")

    cnt = 0
    chk = False
    for i in data:
        if len(i) >= 3:
            chk = True
            break

        if len(i) == 1:
            cnt += 1
        elif len(i) > 1:
            cnt += 2

    print(2 if chk else cnt)
