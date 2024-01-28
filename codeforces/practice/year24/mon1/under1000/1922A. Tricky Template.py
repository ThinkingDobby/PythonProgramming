import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip() for _ in range(3)]

    ans = False
    for i in range(n):
        if data[0][i] != data[2][i] and data[1][i] != data[2][i]:
            ans = True
            break

    print("YES" if ans else "NO")
