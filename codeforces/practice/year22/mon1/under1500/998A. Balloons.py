n = int(input())
data = list(map(int, input().split()))
sdata = sorted(data)
if sum(data) - sdata[0] == sdata[0] or n == 1:
    print(-1)
else:
    print(1)
    print(data.index(sdata[0]) + 1)