n = int(input())
data = list(map(int, input().split()))

negs = 0
tot = 0
ans = []

for i in range(n):
    tot += 1
    if data[i] < 0:
        negs += 1
    if negs == 3:
        ans.append(tot - 1)
        tot = 1
        negs = 1
    if i == n - 1:
        ans.append(tot)

print(len(ans))
print(*ans)