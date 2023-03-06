import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()

    a = s + t[::-1]

    ans = True
    cnt = 0
    for i in range(n + m - 1):
        if a[i] == a[i + 1]:
            cnt += 1
            if cnt > 1:
                ans = False
                break
    print("YES" if ans else "NO")