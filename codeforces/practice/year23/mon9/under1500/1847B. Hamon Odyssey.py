import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = data[0]
    for i in range(1, n):
        tmp &= data[i]

    if tmp != 0:
        print(1)
    else:
        now = data[0]
        cnt = 0
        for i in range(n):
            now &= data[i]
            if now == tmp:
                cnt += 1
                if i != n - 1:
                    now = data[i + 1]

        print(cnt)