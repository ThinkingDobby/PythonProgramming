import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(list(map(int, input().split())) for _ in range(n))

    mv = -1
    cnt = 0

    for i in range(n):
        mv = max(mv, max(data[i]))
        cnt += min(data[i])

    print(cnt * 2 + mv * 2)

