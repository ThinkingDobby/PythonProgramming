n = int(input())
data = []
for i in range(n):
    tmp = input().split()
    data.append((tmp[0], int(tmp[1])))

data.sort(key=lambda x:x[1])

for i in range(n):
    print(data[i][0], end=' ')