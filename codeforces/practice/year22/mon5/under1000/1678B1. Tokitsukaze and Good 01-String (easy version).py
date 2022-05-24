import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().rstrip()) + ['a']

    ans = 0
    cnt = 1
    for i in range(1, n + 1):
        if data[i - 1] != data[i]:
            if cnt % 2 == 1:
                ans += 1
                cnt = 2
            else:
                cnt = 1
        else:
            cnt += 1

    print(ans)
