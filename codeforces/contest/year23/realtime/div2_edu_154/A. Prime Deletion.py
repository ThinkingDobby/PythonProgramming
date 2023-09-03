import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    i1 = data.index('1')
    i3 = data.index('3')

    if i1 > i3:
        print(31)
    else:
        print(13)