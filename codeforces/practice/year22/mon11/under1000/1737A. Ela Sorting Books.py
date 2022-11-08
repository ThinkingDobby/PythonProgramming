# rte

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, y = map(int, input().split())

    data = list(input().rstrip())
    chk = [0] * 26
    for i in data:
        chk[ord(i) - 97] += 1
    for i in range(1, 26):
        chk[i] = min(chk[i], chk[i - 1])

    ans = ""
    now = 0
    for i in range(a // y - 1, -1, -1):
        tmp = chk[i] - now
        ans += chr(97 + i + 1) * tmp
        now += tmp

    print(ans[:y] + 'a' * max(0, y - len(ans)))