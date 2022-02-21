n, f, s = map(int, input().split())
data = list(map(int, input().split()))

w = 0
b = 0
d = 0
flag = True
for i in range(n // 2):
    if data[i] == data[-(i + 1)]:
        if data[i] + data[-(i + 1)] != 4:
            continue
        else:
            d += 2
    elif data[i] + data[-(i + 1)] == 2:
        w += 1
    elif data[i] + data[-(i + 1)] == 3:
        b += 1
    else:
        flag = False
        break

if not flag:
    print(-1)
else:
    if n % 2 == 1 and data[n // 2] == 2:
        d += 1
    print(min(f * w + s * b + d * f, f * w + s * b + d * s))