import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    now = False
    ans = True
    i = 0
    while i < n:
        if now:
            if i == n - 1 or data[i] != data[i + 1]:
                ans = False
            now = False
            i += 1
        else:
            now = True
        i += 1

    print("YES" if ans else "NO")