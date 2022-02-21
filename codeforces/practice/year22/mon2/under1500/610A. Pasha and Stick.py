n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = (n // 2 + 1) // 2 - 1
    print(ans)