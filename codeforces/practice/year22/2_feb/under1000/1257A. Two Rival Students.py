for _ in range(int(input())):
    n, x, a, b = map(int, input().split())
    print(min(x + abs(b - a), n - 1))