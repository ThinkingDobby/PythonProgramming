import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k, n = map(int, input().split())
    now = 1
    i = 0

    chk = set()
    while True:
        now += i
        if i >= k or now >= n:
            break
        chk.add(now)
        i += 1

    cnt = k - i
    for i in range(n, 0, -1):
        if cnt <= 0:
            break
        if i not in chk:
            chk.add(i)
            cnt -= 1

    print(*sorted(chk))

