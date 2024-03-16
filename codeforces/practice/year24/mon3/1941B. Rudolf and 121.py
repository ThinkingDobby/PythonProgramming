import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = True
    for i in range(n - 2):
        if data[i] == 0:
            continue

        if data[i + 1] - data[i] * 2 < 0 or data[i + 2] - data[i] < 0:
            ans = False
            break
        else:
            data[i + 1] -= data[i] * 2
            data[i + 2] -= data[i]
            data[i] = 0

    if any(data):
        ans = False

    print("YES" if ans else "NO")

