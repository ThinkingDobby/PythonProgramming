import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    if data[1] == 'b':
        print(data[0], data[1:-1], data[-1])
    else:
        print(data[0], data[1], data[2:])