import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = sum(data) // n
    now = 0
    ans = True
    for i in range(n):
        if data[i] < tmp:
            if now >= tmp - data[i]:
                now -= tmp - data[i]
            else:
                ans = False
                break
        else:
            now += data[i] - tmp

    print("YES" if ans else "NO")