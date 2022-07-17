import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    i1 = 0
    i0 = len(s) - 1
    if '1' in s:
        i1 = s.rindex('1')
    if '0' in s:
        i0 = s.find('0')

    if i1 < i0:
        print(i0 - i1 + 1)
    else:
        print(1)