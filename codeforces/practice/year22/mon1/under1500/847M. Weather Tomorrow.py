n = int(input())
data = list(map(int, input().split()))

flag = True
gap = data[1] - data[0]
for i in range(1, n):
    if data[i] - data[i - 1] != gap:
        flag = False
        break

if not flag:
    print(data[-1])
else:
    print(data[-1] + gap)