for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    m = max(data)

    ans = []
    if n == 1:
        print(n)
    elif data[0] != m and data[-1] != m:
        print(-1)
    else:
        if data[0] == m:
            print(" ".join(map(str, data[0:1] + data[1::][::-1])))
        else:
            print(" ".join(map(str, data[:-1][::-1] + data[-1::])))

