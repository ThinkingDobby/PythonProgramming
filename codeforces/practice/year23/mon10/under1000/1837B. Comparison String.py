import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip() + '*'
    cnt_1 = 0
    cnt_2 = 0

    cnt = 1

    for i in range(1, n + 1):
        if data[i - 1] != data[i]:
            if data[i - 1] == '<':
                cnt_1 = max(cnt_1, cnt)
            else:
                cnt_2 = max(cnt_2, cnt)
            cnt = 1
        else:
            cnt += 1

    print(max(cnt_1, cnt_2) + 1)

