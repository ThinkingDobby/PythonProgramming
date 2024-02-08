import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip())

    f = s = -1

    for i in range(n):
        if data[i] == 'B' and f == -1:
            f = i

        if data[i] == 'B':
            s = i

    print(s - f + 1)