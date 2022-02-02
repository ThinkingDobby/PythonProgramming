data = list(input())
cnt = 0
for i in range(len(data) // 2):
    if data[i] != data[-(i + 1)]:
        cnt += 1
if cnt == 1:
    print("YES")
elif cnt == 0 and len(data) % 2 == 1:
    print("YES")
else:
    print("NO")