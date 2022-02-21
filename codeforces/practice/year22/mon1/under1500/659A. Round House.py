n, a, b = map(int, input().split())
ans = (a + b + n - 1) % n + 1
print(ans)