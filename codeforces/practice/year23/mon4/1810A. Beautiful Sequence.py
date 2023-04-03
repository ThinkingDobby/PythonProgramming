import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk = False
    for i in range(n):
        if data[i] <= i + 1:
            chk = True

    print("YES" if chk else "NO")