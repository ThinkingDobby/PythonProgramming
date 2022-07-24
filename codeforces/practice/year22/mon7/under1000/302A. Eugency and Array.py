import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

cnt1 = data.count(1)
cnt0 = data.count(-1)

for _ in range(m):
    l, r = map(int, input().split())
    tmp = r - l + 1
    if tmp % 2 == 1:
        print(0)
    else:
        if tmp // 2 <= min(cnt1, cnt0):
            print(1)
        else:
            print(0)