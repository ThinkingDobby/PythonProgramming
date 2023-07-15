import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    data = sorted(map(int, input().split()))
    ans = True
    for i in range(n):
        if data[i + n] - data[i] < x:
            ans = False
            break

    print("YES" if ans else "NO")