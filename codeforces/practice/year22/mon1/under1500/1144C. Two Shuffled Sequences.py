n = int(input())
data = list(map(int, input().split()))

a = set()
b = set()

flag = True
for i in range(n):
    if data[i] in a:
        if data[i] in b:
            flag = False
            break
        else:
            b.add(data[i])
    else:
        a.add(data[i])

if flag:
    print("YES")
    print(len(a))
    print(*sorted(a))
    print(len(b))
    print(*sorted(b, reverse=True))
else:
    print("NO")