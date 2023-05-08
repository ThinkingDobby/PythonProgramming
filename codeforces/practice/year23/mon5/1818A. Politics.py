import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    data = input().rstrip()
    cnt = 1

    for _ in range(n - 1):
        now = input().rstrip()
        if now == data:
            cnt += 1

    print(cnt)