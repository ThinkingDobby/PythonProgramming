import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    data = input().rstrip()

    fz = data.find('0')
    lz = data.rfind('0')
    fo = data.find('1')
    lo = data.rfind('1')

    for _ in range(q):
        l, r = map(int, input().split())
        ans = False
        if data[l - 1] == '0':
            if fz != -1 and fz < l - 1:
                ans = True
        else:
            if fo != -1 and fo < l - 1:
                ans = True
        if data[r - 1] == '0':
            if lz != -1 and lz > r - 1:
                ans = True
        else:
            if lo != -1 and lo > r - 1:
                ans = True

        print("YES" if ans else "NO")