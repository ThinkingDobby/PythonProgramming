for _ in range(int(input())):
    n, k = map(int, input().split())
    data = sorted(map(int, input().split()), reverse=True)
    print(sum(data[:k + 1]))