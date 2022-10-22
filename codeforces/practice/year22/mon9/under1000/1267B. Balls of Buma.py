import sys

input = sys.stdin.readline

data = '0' + input().rstrip()

memo = []

i = 1
while i < len(data):
    if data[i - 1] != data[i]:
        now = data[i]
        cnt = 1
        i += 1
        while i < len(data) and data[i] == now:
            i += 1
            cnt += 1
        memo.append([now, cnt])

if len(memo) % 2 == 0:
    print(0)
else:
    ans = True
    for i in range(len(memo) // 2):
        if memo[i][0] != memo[len(memo) - 1 - i][0] or memo[i][1] + memo[len(memo) - 1 - i][1] < 3:
            ans = False
            break
    if memo[len(memo) // 2][1] < 2:
        ans = False
    print(memo[len(memo) // 2][1] + 1 if ans else 0)
