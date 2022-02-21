n, k = map(int, input().split())
ans = min(k - 1, n - k) + n - 1 + n * 2 + 1
print(ans)