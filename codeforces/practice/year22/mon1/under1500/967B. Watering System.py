n, A, B = map(int, input().split())
s = list(map(int, input().split()))
tmp = s[0] * A / B - s[0]

idx = n - 1
sum_s = sum(s[1:])
ss = sorted(s[1:], reverse=True)
for i in range(n - 1):
    if sum_s <= tmp:
        idx = i
        break
    sum_s -= ss[i]

print(idx)