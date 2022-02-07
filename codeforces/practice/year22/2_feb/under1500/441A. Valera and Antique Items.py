n, v = map(int, input().split())
ans = []

for i in range(n):
    tmp = list(map(int, input().split()))
    if min(tmp[1:]) + 1 <= v:
        ans.append(i + 1)

print(len(ans))
print(*ans)