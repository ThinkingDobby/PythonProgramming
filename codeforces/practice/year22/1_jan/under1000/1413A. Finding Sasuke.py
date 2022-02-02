for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    for i in range(n // 2, n):
        print(-data[i], end=' ')
    for i in range(n // 2):
        print(data[i], end=' ')
    print()