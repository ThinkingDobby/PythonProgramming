import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    if data[0] == '?':
        tmp = (data + '*').lstrip('?')[0]
        prev = '0' if tmp == '*' else tmp

        data = list(data)
        data[0] = prev
    else:
        data = list(data)

    for i in range(1, len(data)):
        if data[i] == '?':
            data[i] = data[i - 1]

    print(''.join(data))
