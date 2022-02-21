data = sorted(map(int, input().split()))
if data[0] + data[3] == data[1] + data[2] or sum(data[:3]) == data[3]:
    print("YES")
else:
    print("NO")