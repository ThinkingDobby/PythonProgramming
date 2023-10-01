import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = [input().rstrip() for _ in range(10)]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == 'X':
                a = min(i, 10 - i - 1)
                b = min(j, 10 - j - 1)
                cnt += min(a, b) + 1

    print(cnt)
