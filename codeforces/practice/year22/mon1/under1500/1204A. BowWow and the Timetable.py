s = input()
l = len(s)

ans = -1
if l % 2 == 1:
    if l == 1:
        ans = 0
    elif '1' not in s[1:]:
        ans = l // 2
    else:
        ans = (l + 1) // 2
else:
    ans = l // 2

print(ans)