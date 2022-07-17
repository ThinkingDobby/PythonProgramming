import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    f = -1
    s = -1
    for i in range(1, n):
        if data[i - 1] == data[i]:
            if f == -1:
                f = i
            else:
                s = i - 1

    if f == s == -1:
        print(0)
    elif s == -1:
        print(0)
    else:
        print(max(s - f, 1))

