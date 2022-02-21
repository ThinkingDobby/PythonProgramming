n = int(input())
data = list(map(int, input().split())) + [0]

i = 1
cnt = 0
while i < n:
    if data[i - 1] == data[i + 1] == 1 and data[i] == 0:
        i += 2
        if i >= n:
            cnt += 1
            break
        if data[i - 1] == data[i + 1] == 1 and data[i] == 0:
            i += 1
        cnt += 1

    i += 1

print(cnt)