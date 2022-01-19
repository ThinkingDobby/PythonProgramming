for _ in range(int(input())):
    n = int(input())
    print(n)
    print(*[i + 1 for i in range(n)])