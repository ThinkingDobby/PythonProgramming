import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    ans = False
    for _ in range(n):
        data = [list(map(int, input().split())) for _ in range(2)]
        if data[0][1] == data[1][0]:
            ans = True

    if m % 2 == 0:
        print("YES" if ans else "NO")
    else:
        print("NO")