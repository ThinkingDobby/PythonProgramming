for _ in range(int(input())):
    n, k = map(int, input().split())
    data = sorted(map(int, input().split()))
    mv = data[0]
    s = 0
    for i in range(1, n):
        s += (k - data[i]) // mv
    print(max(0, s))