n = int(input())
data = input()

cnt = 0
ans = ''
for i in range(0, n, 2):
    if len({data[i], data[i + 1]}) == 1:
        cnt += 1
        ans += 'ab'
    else:
        ans += data[i] + data[i + 1]

print(cnt)
print(ans)