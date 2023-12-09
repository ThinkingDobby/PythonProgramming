import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    data = sorted(map(int, input().split()))

    now = b
    ans = 0
    for i in range(n):
        if now + data[i] <= a:
            now += data[i]
        else:
            ans += now - 1
            now = a

    ans += now

    print(ans)
