for _ in range(int(input())):
    n, k = map(int, input().split())
    for i in range(n):
        print(chr(99 - i % 3), end='')
    print()