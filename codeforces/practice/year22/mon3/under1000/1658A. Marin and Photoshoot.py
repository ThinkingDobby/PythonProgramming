import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip()) + [1, 1]
    cnt = 0
    if n == 1:
        print(0)
    elif n == 2:
        print(2 if data[0] == data[1] == '0' else 0)
    else:
        for i in range(n):
            if data[i] == '0':
                if data[i + 1] == '0':
                    cnt += 2
                elif data[i + 1] == '1' and data[i + 2] == '0':
                    cnt += 1

        print(cnt)
