data = list(map(int, input().split()))

flag = False
for i in range(len(data) - 2):
    for j in range(i + 1, len(data) - 1):
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == sum(data) / 2:
                flag = True
                break

if flag:
    print("YES")
else:
    print("NO")