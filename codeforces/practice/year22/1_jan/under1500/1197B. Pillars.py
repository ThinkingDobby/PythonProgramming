n = int(input())
data = list(map(int, input().split()))

cl = False
check = True
for i in range(1, n):
    if data[i - 1] > data[i]:
        cl = True
    if cl and data[i - 1] < data[i]:
        check = False

if check:
    print("YES")
else:
    print("NO")