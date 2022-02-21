for _ in range(int(input())):
    n, x = map(int, input().split())
    data = list(map(int, input().split()))
    if sum(data) == x:
        print("NO")
    else:
        s = 0

        print("YES")
        for i in range(n):
            if s + data[i] == x:
                data[i], data[i + 1] = data[i + 1], data[i]
            s += data[i]
            print(data[i], end=' ')
        print()