for _ in range(int(input())):
    data = list(map(int, input()))

    if sum(data) % 3 == 0 and 0 in data:
        if data.count(0) > 1 or 2 in data or 4 in data or 6 in data or 8 in data:
            print("red")
        else:
            print("cyan")
    else:
        print("cyan")