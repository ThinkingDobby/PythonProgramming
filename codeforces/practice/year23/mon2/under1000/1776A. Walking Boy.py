import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split())) + [1440]

    cnt = 0
    for i in range(1, n + 2):
        if data[i] - data[i - 1] >= 120:
            cnt += 1
            if data[i] - data[i - 1] >= 240:
                cnt += 1

    print("YES" if cnt >= 2 else "NO")