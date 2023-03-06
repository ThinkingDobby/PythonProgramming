import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    odd = True if data[0] % 2 == 1 else False
    cnt = 0

    for i in range(1, n):
        now = True if data[i] % 2 == 1 else False
        if odd == now:
            cnt += 1

        odd = now

    print(cnt)