n, k = map(int, input().split())
tmp = (k - 1) // 2
ans = min(tmp, max(0, tmp - (k - (n + 1))))
print(ans)