k = int(input())
l = int(input())

i = 1
flag = False
while l >= k**i:
    if k**i == l:
        flag = True
        break
    i += 1

if flag:
    print("YES")
    print(i - 1)
else:
    print("NO")