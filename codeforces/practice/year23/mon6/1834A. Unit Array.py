import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    check = n // 2
    if check % 2 == 1:
        check -= 1

    cnt = len([i for i in data if i == -1])

    if cnt >= check:
        print(cnt - check)
    else:
        print(1 if cnt % 2 == 1 else 0)