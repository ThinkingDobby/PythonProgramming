import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    prev = 0
    cnt = 0

    for i in range(len(data)):
        if data[i] == '0':
            tmp = i - prev + 1
            cnt += tmp if tmp > 1 else 0
            prev += 1

    print(cnt)
