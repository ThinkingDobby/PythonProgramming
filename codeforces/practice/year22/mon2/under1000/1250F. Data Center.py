n = int(input())
ans = 1
for i in range(2, n):
    if n // i < i:
        break
    if n % i == 0:
        ans = i

print((ans + n // ans) * 2)
