import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().split()
    n = int(data[0])
    c = data[1]

    s = input().rstrip()

    if c == 'g':
        print(0)
    else:
        s += s

        now = -1
        ans = -1
        for i in range(n * 2):
            if s[i] == 'g' and now != -1:
                ans = max(ans, i - now)
                now = -1
            elif s[i] == c and now == -1:
                now = i

        print(ans)
