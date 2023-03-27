import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    now = 1
    ans = 0
    for i in range(n):
        if data[i] < now:
            continue
        elif data[i] == now:
            now += 1
        else:
            ans += data[i] - now
            now += 1

    print(ans)