for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    print(min(sum(data), m))