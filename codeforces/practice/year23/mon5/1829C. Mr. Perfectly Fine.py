import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(input().split()) for _ in range(n)]

    ans = []

    f = sorted([int(data[i][0]) for i in range(n) if data[i][1] == "11"])
    s = sorted([int(data[i][0]) for i in range(n) if data[i][1] == "01"])
    t = sorted([int(data[i][0])for i in range(n) if data[i][1] == "10"])

    if f:
        ans.append(f[0])
    if s and t:
        ans.append(s[0] + t[0])

    print(min(ans) if ans else -1)