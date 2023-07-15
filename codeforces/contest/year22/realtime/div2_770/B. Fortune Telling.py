for _ in range(int(input())):
    n, x, y = map(int, input().split())
    data = list(map(int, input().split()))
    res = x % 2
    for i in range(n):
        res = (res ^ data[i]) % 2
    if res == y % 2:
        print("Alice")
    else:
        print("Bob")