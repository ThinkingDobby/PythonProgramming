import sys

input = sys.stdin.readline

s = ''
i = 1
while True:
    if len(s) > 1000:
        break
    else:
        s += str(i)
    i += 1

print(s[int(input()) - 1])