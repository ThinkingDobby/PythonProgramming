import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, s = map(int, input().split())
    data = list(map(int, input().split()))

    tmp = max(data)
    rest = tmp * (tmp + 1) // 2 - sum(data)

    s -= rest
    if s < 0:
        print("NO")
    elif s == 0:
        print("YES")
    else:
        now = 0
        ans = False
        for i in range(tmp + 1, 1000):
            now += i
            if now == s:
                ans = True
                break

        print("YES" if ans else "NO")
