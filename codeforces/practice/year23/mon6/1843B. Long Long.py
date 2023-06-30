import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    s = sum(map(abs, data))
    data += [1]

    cnt = 0
    check = data[0] < 0
    for i in range(1, n + 1):
        if check:
            if data[i] > 0:
                check = False
                cnt += 1
        else:
            if data[i] < 0:
                check = True

    print(s, cnt)
