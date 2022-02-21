n = int(input())
data = input()
flag = False
for i in range(1, n):
    if data[i - 1] != data[i]:
        flag = True
        print("YES")
        print(data[i - 1] + data[i])
        break

if not flag:
    print("NO")