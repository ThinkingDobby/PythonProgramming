import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    sdata = sorted(data)

    if data == sorted(data):
        print(0)
    else:
        tmp = -1
        for i in range(n - 1, -1, -1):
            if data[i] != sdata[i]:
                tmp = i
                break

        print(max(data[:tmp + 1]))