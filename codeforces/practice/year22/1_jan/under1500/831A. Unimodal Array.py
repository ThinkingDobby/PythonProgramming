n = int(input())
data = list(map(int, input().split()))
if n > 1:
    if data[-2] >= data[-1]:
        data.append(data[-1] + 1)
    else:
        data.append(data[-1] - 1)

asc = False
dec = False
con = False
flag = True

for i in range(1, n):
    if data[i] == data[i - 1] and not data[i + 1] == data[i]:
        if dec or con:
            flag = False
            break
        con = True
    elif data[i] < data[i - 1] and not data[i + 1] < data[i]:
        if dec:
            flag = False
            break
        dec = True
    elif data[i] > data[i - 1] and not data[i + 1] > data[i]:
        if asc or con or dec:
            flag = False
            break
        asc = True

if flag:
    print("YES")
else:
    print("NO")