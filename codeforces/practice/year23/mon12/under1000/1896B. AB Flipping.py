import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip())

    chk = False
    cnt = 0
    for i in data:
        if i == 'A':
            chk = True
        elif chk:
            cnt += 1

    chk = False
    for i in data[::-1]:
        if i == 'B':
            chk = True
        elif chk:
            cnt += 1

    print(max(0, cnt - 1))