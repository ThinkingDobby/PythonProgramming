import sys

for t in range(int(input())):
    n, m, rb, cb, rd, cd = list(map(int, input().split(" ")))
    ans = sys.maxsize
    tmp = cd - cb
    if tmp > 0: ans = tmp
    tmp = rd - rb
    if tmp > 0:
        ans = min(ans, tmp)
    if cd - cb == 0 or rd - rb == 0: ans = 0
    ans = min(ans, m - cb + m - cd, n - rb + n - rd)
    print(ans)
    