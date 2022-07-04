import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = input().rstrip()
    cnt = data[:k].count('W')
    mv = cnt

    for i in range(k, n):
        if data[i] == 'W':
            cnt += 1
        if data[i - k] == 'W':
            cnt -= 1
        mv = min(mv, cnt)

    print(mv)