a, b = input().split()
ans = a[0]
for i in a[1:]:
    if i < b[0]:
        ans += i
    else:
        break
ans += b[0]
print(ans)