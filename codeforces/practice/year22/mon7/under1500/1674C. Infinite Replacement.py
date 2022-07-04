import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    t = input().rstrip()

    if t == 'a':
        print(1)
    elif 'a' in t:
        print(-1)
    else:
        cnt = 1
        l = len(s)
        for i in range(1, l + 1):
            cnt += math.comb(l, i)
        print(cnt)