s = input()
k = int(input())
w = list(map(int, input().split()))
l = len(s)
mv = max(w)

ans = sum([w[ord(s[i]) - 97] * (i + 1) for i in range(l)])
for i in range(k):
    ans += (i + l + 1) * mv

print(ans)