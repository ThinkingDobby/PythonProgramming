n = int(input())
data = [0] + list(map(int, input().split()))
day = 0
now = 1
while True:
    day += 1
    mv = data[now]
    while True:
        if now == mv:
            break
        now += 1
        mv = max(mv, data[now])

    if now >= n:
        break
    now += 1

print(day)
