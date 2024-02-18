import sys

input = sys.stdin.readline

for _ in range(int(input())):
    ans = False

    a, b = map(int, input().split())

    if a % 2 == 0:
        if a // 2 != b or b * 2 != a:
            ans = True

    if b % 2 == 0:
        if b // 2 != a or a * 2 != b:
            ans = True

    print("YES" if ans else "NO")