n = int(input())
data = input()
cnt = 0
for i in range(n):
    if data[i] == '-':
        cnt = max(cnt - 1, 0)
    else:
        cnt += 1

print(cnt)