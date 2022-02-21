n = int(input())
s = input()

cnt = 0
for i in range(n):
    cnt += (i + 1) if int(s[i]) % 2 == 0 else 0
print(cnt)