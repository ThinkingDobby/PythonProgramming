import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().rstrip()))
    cnt0 = data.count(0)
    cnt1 = data.count(1)

    if cnt0 < cnt1:
        ans = cnt0 - data[:cnt0 * 2].count(0) + len(data) - cnt0 * 2
    else:
        ans = cnt1 - data[:cnt1 * 2].count(1) + len(data) - cnt1 * 2

    print(ans)