import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    left = [a]
    cnt = 0
    for i in range(n,  0, -1):
        if i not in (a, b):
            cnt += 1
            left.append(i)
            if cnt == n // 2 - 1:
                break

    right = [b]
    cnt = 0
    for i in range(1, n + 1):
        if i not in (a, b):
            cnt += 1
            right.append(i)
            if cnt == n // 2 - 1:
                break

    if a > min(left) or b < max(right):
        print(-1)
    else:
        print(*left, *right)