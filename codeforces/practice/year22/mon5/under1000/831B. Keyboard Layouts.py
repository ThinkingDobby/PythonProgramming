import sys

input = sys.stdin.readline

f = input().rstrip()
s = input().rstrip()

data = input().rstrip()
for i in data:
    if i.islower():
        print(s[f.find(i)], end='')
    elif i.isupper():
        print(s[f.find(i.lower())].upper(), end='')
    else:
        print(i, end='')