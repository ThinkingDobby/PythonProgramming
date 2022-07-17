import sys

input = sys.stdin.readline


def get_min(s):
    return int(s[:2]) * 60 + int(s[3:])


def time_add(now, x):
    now += x
    h = now // 60
    m = now % 60
    if h >= 24:
        h %= 24

    return "%02d:%02d" % (h, m)


for _ in range(int(input())):
    s, x = input().split()
    x = int(x)

    now = get_min(s)
    times = set()
    ans = set()
    while now not in times:
        times.add(now)
        tmp = time_add(now, x)
        if tmp == tmp[::-1]:
            ans.add(tmp)
        now = get_min(tmp)

    print(len(ans))