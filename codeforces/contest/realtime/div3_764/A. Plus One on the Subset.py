for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    print(max(data) - min(data))
