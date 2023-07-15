import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    mv = -1
    cnt = 0
    ans = 0
    for i in range(n):
        mv = max(mv, data[i])
        cnt += 1

        if mv == cnt:
            ans += 1

    print(ans)

