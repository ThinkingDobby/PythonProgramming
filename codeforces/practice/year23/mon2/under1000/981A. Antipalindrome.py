import sys

input = sys.stdin.readline

data = input().rstrip()

if data == data[::-1]:
    if len(set(data)) == 1:
        print(0)
    else:
        print(len(data) - 1)
else:
    print(len(data))