import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

r_memo = [0 for _ in range(n)] # 오른쪽 방향으로
l_memo = [0 for _ in range(n)]

for i in range(1, n):
    if data[i] < data[i - 1]:
        r_memo[i] = r_memo[i - 1] + data[i - 1] - data[i]
    else:
        r_memo[i] = r_memo[i - 1]

    if data[n - 1 - i] < data[n - i]:
        l_memo[n - 1 - i] = l_memo[n - i] + data[n - i] - data[n - 1 - i]
    else:
        l_memo[n - 1 - i] = l_memo[n - i]

for i in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if s < t:
        ans = r_memo[t] - r_memo[s]
    else:
        ans = l_memo[t] - l_memo[s]

    print(ans)