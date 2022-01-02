for t in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    if sum(a) % len(a) == 0:
        print(0)
    else:
        print(1)