import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r, a, = map(int, input().split())

    f = r // a + r % a
    tmp = (r // a - 1) * a + a - 1
    if tmp >= l:
        s = tmp // a + tmp % a
        print(max(f, s))
    else:
        print(f)