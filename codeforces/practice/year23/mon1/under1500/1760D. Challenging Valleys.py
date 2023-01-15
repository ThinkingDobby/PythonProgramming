import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    inc = False
    ans = True

    for i in range(1, n):
        if data[i - 1] < data[i]:
            inc = True
        elif data[i - 1] > data[i] and inc:
            ans = False

    print("YES" if ans else "NO")
