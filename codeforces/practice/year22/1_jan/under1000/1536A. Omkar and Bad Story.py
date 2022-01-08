for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if min(data) < 0:
        print("No")
    else:
        print("Yes")
        print(max(data) + 1)
        print(*[i for i in range(0, max(data) + 1)])