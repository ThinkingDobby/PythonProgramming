n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

mv = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        mv = max(mv, ((data[i][0] - data[j][0])**2 + (data[i][1] - data[j][1])**2)**(1/2))

print(mv)