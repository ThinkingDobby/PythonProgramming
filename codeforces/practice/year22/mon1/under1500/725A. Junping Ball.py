n = int(input())
data = list(input())
cnt = 0
for i in range(0, n):
    if data[i] == '>':
        break
    cnt += 1
for i in range(n - 1, -1, -1):
    if data[i] == '<':
        break
    cnt += 1

print(cnt)