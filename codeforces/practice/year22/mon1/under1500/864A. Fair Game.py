n = int(input())
data = [int(input()) for _ in range(n)]
if len(set(data)) == 2:
    if len(data) / 2 == data.count(data[0]):
        print("YES")
        print(*list(set(data)))
    else:
        print("NO")
else:
    print("NO")