n = int(input())
data = sorted(map(int, input().split()))
cnt = 0

if n > 1:
    i = 1
    while True:
        if data[i] == data[i - 1]:
            cnt += 1
            i += 1
        i += 1
        if i >= n:
            break

print(cnt // 2)