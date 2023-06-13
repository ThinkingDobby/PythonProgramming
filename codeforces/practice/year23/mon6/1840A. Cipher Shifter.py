import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip())

    memo = []
    now = "0"
    chk = False

    for i in range(n):
        if data[i] == now and chk:
            chk = False
        elif not chk:
            chk = True
            now = data[i]
            memo.append(data[i])

    print(''.join(memo))