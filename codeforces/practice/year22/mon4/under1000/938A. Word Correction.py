import sys

input = sys.stdin.readline

vows = ['a', 'e', 'i', 'o', 'u', 'y']

n = int(input())
data = input().rstrip()
vow = False
for i in data:
    if vow:
        if i in vows:
            continue
        else:
            print(i, end='')
            vow = False
    else:
        print(i, end='')
        if i in vows:
            vow = True
