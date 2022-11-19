import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip()) + ['3']

    now = data[0]
    cnt = 1
    mv = -1
    for i in range(1, n + 1):
        if now != data[i]:
            now = data[i]
            mv = max(cnt, mv)
            cnt = 1
        else:
            cnt += 1

    tmp = data.count('0')
    print(max(tmp * (n - tmp), mv**2))