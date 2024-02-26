import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    cnt = 0
    ans = 0

    for i in range(n):
        if data[i] == '*':
            cnt += 1
        else:
            cnt = 0

        if data[i] == '@':
            ans += 1

        if cnt >= 2:
            break

    print(ans)