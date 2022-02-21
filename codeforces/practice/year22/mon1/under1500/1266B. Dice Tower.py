n = int(input())
data = list(map(int, input().split()))

for i in range(n):
    ans = False
    for j in range(1, 7):
        if data[i] > 14 and (data[i] - j) % 14 == 0:
            ans = True
            break
    if ans:
        print("YES")
    else:
        print("NO")