for _ in range(int(input())):
    sum = int(input())
    for _ in range(int(input())):
        a, b = map(int, input().split())
        sum += a * b
    print(sum)