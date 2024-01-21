import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    f = input().rstrip()
    s = input().rstrip()

    cnt_1 = 0
    cnt_0 = 0
    for i in range(n):
        if f[i] != s[i]:
            if f[i] == '1':
                cnt_1 += 1
            else:
                cnt_0 += 1

    print(max(cnt_1, cnt_0))
