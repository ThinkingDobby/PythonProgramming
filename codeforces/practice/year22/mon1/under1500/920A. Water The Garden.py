for _ in range(int(input())):
    n, k = map(int, input().split())
    data = sorted(map(int, input().split()))
    mv = -1
    for i in range(k - 1):
        mv = max(mv, (data[i + 1] - data[i]) // 2 + 1)
    print(max(data[0], n - data[-1] + 1, mv))
