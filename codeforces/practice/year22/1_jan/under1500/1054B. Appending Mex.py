n = int(input())
data = list(map(int, input().split()))
mv = -1
flag = True
for i in range(n):
    if data[i] == mv + 1 or data[i] <= mv:
        mv = max(mv, data[i])
    else:
        print(i + 1)
        flag = False
        break

if flag:
    print(-1)