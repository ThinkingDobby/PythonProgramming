import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(input().rstrip())

    cnt_0 = data.count('0')
    cnt_1 = data.count('1')

    for i in data:
        if i == '0':
            if cnt_1 <= 0:
                break
            cnt_1 -= 1
        elif i == '1':
            if cnt_0 <= 0:
                break
            cnt_0 -= 1

    print(cnt_0 + cnt_1)
