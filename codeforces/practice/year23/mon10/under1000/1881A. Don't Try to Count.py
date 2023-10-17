import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input().rstrip()
    s = input().rstrip()

    tmp = x
    cnt = 0
    ans = False
    while True:
        if s in tmp:
            ans = True
            break

        if len(tmp) > len(s) * 2 and cnt > 1:
            break

        tmp *= 2
        cnt += 1

    print(-1 if not ans else cnt)