import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    if len(set(data)) == 1:
        print(-1)
    else:
        print(len(data) - 1 if data == data[::-1] else len(data))
