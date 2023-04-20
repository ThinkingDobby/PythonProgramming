import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    cnt = 1 if data[0] == '_' else 0
    for i in range(1, len(data)):
        if data[i] == '_' and data[i - 1] == '_':
            cnt += 1

    if data[-1] == '_':
        cnt += 1

    if len(data) == 1 and data[0] == '^':
        cnt += 1

    print(cnt)
