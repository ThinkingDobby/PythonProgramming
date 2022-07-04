import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n):
        tmp = data[i] - data[i - 1]
        if tmp > 3:
            cnt = 3
            break
        elif tmp == 3:
            cnt += 2
        elif tmp == 2:
            cnt += 1
        if cnt > 2:
            break

    print("YES" if cnt <= 2 else "NO")