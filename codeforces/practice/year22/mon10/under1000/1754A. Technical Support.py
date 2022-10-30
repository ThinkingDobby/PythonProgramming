import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    cnt = 0
    for i in range(n):
        if data[i] == 'Q':
            cnt += 1
        else:
            cnt = max(0, cnt - 1)

    print("NO" if cnt > 0 else "YES")
