for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if len(set(data)) == 1:
        print(n)
    else:
        print(1)