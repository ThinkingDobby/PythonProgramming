for _ in range(int(input())):
    data = input()
    if len(data) == len(set(data)):
        if ord(max(data)) - ord(min(data)) + 1 == len(data):
            print("Yes")
        else:
            print("No")
    else:
        print("No")