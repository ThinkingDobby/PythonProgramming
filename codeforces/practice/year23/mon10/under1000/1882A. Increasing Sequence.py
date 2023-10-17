import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ni = 1
    cnt = 0
    while True:
        if ni == data[cnt]:
            ni += 1
            continue

        cnt += 1
        if cnt >= n:
            break
        ni += 1

    print(ni)