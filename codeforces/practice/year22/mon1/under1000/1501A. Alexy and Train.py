import math

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.insert(0, [0, 0])
    tm = list(map(int, input().split()))

    now = 0
    for i in range(1, n + 1):
        now += data[i][0] - data[i - 1][1] + tm[i - 1]
        if i == n:
            break
        tmp = now + int(math.ceil((data[i][1] - data[i][0]) / 2))
        now = max(tmp, data[i][1])

    print(now)