n = int(input())
data = list(input())

idx = -1
for i in range(1, n):
    if data[i - 1] > data[i]:
        idx = i
        break

if idx == -1:
    print("NO")
else:
    print("YES")
    print(idx, idx + 1)
