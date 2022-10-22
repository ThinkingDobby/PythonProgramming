import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    f = []
    s = []

    for i in range(n):
        if a[i] == 0:
            f.append(b[i])
        else:
            s.append(b[i])

    f.sort(reverse=True)
    s.sort(reverse=True)
    sv = 0
    if len(f) > len(s):
        sv += sum(s) * 2
        sv += sum(f[:len(s)]) * 2 + sum(f[len(s):])
    elif len(f) < len(s):
        sv += sum(f) * 2
        sv += sum(s[:len(f)]) * 2 + sum(s[len(f):])
    else:
        sv = sum(f) * 2 + sum(s) * 2 - min(min(f), min(s))
    print(sv)
