import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    i = 1
    cnt = 0
    while n > 1:
        if data[i - 1] > data[i]:
            cnt += 1
            i += 1
        i += 1
        if i >= n:
            break

    print(cnt)