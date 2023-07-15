import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    chk = set()
    l = 0

    cnt = 0
    for i in s:
        if i not in chk:
            if l >= 3:
                cnt += 1
                l = 0
                chk = set()
            chk.add(i)
            l += 1

    if l > 0:
        cnt += 1
    print(cnt)